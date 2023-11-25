-- DROP TABLE IF EXISTS shelter, "user", employee_user, employee_user_in_shelter, abstract_pet, pet_instance, pet_takeout_request CASCADE;
-- DROP TYPE IF EXISTS pet_takeout_request_status;
-- DROP INDEX IF EXISTS "UQ_pet_takeout_request_can_be_resolved_only_once";
CREATE TYPE pet_takeout_request_status AS enum('undecided', 'approved', 'rejected');



CREATE TABLE shelter (
  shelter_id INTEGER GENERATED ALWAYS AS IDENTITY NOT NULL,
  name TEXT NOT NULL,
  address TEXT NOT NULL,
  PRIMARY KEY (shelter_id),
  CONSTRAINT "UQ_shelter_address" UNIQUE (address)
);


CREATE TABLE "user" (
  user_id INTEGER GENERATED ALWAYS AS IDENTITY NOT NULL,
  first_name TEXT NOT NULL,
  second_name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL,
  PRIMARY KEY (user_id),
  CONSTRAINT "UQ_user_email" UNIQUE (email),
  CONSTRAINT "UQ_user_phone" UNIQUE (phone)
);

CREATE TABLE employee_user (
  employee_user_id INTEGER NOT NULL,
  password_salt char(32) NOT NULL,
  password_hash char(32) NOT NULL,
  work_email TEXT NOT NULL,

  PRIMARY KEY (employee_user_id),
  CONSTRAINT "UQ_employee_user.work_email" UNIQUE (work_email),

  CONSTRAINT "FK_employee_user.employee_user_id"
    FOREIGN KEY (employee_user_id)
      REFERENCES "user"(user_id)
);

CREATE TABLE employee_user_in_shelter (
  shelter_id INTEGER NOT NULL,
  employee_user_id INTEGER NOT NULL,
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  employed_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
  employee_position TEXT NOT NULL,
  PRIMARY KEY (shelter_id, employee_user_id),

  CONSTRAINT "FK_employee_user_in_shelter.shelter_id"
    FOREIGN KEY (shelter_id)
      REFERENCES shelter (shelter_id),

  CONSTRAINT "FK_employee_user_in_shelter.employee_user_id"
    FOREIGN KEY (employee_user_id)
      REFERENCES "employee_user" (employee_user_id)
);

CREATE TABLE abstract_pet (
  abstract_pet_id INTEGER GENERATED ALWAYS AS IDENTITY NOT NULL,
  parent_abstract_pet_id INTEGER,
  pet_class_name TEXT NOT NULL,
  PRIMARY KEY (abstract_pet_id),
  CONSTRAINT "UQ_abstract_pet.pet_class_name" UNIQUE (pet_class_name),
  CONSTRAINT "FK_abstract_pet.parent_abstract_pet_id"
    FOREIGN KEY (parent_abstract_pet_id)
      REFERENCES abstract_pet (abstract_pet_id)
);

CREATE TABLE pet_instance (
  pet_instance_id INTEGER GENERATED ALWAYS AS IDENTITY NOT NULL,
  shelter_id INTEGER NOT NULL,
  abstract_pet_id INTEGER NOT NULL,
  was_brought_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
  name TEXT NOT NULL,
  PRIMARY KEY (pet_instance_id),
  CONSTRAINT "UQ_pet_instance.pet_instance_in_shelter" UNIQUE (pet_instance_id, shelter_id),

  CONSTRAINT "FK_pet_instance.shelter_id"
    FOREIGN KEY (shelter_id)
      REFERENCES shelter (shelter_id),
  CONSTRAINT "FK_pet_instance.abstract_pet_id"
    FOREIGN KEY (abstract_pet_id)
      REFERENCES abstract_pet (abstract_pet_id)
);



CREATE TABLE pet_takeout_request (
  pet_takeout_request_id INTEGER GENERATED ALWAYS AS IDENTITY NOT NULL,
  adopter_user_id INTEGER NOT NULL,
  shelter_id INTEGER NOT NULL,
  employee_user_id INTEGER NOT NULL,
  pet_instance_id INTEGER NOT NULL,
  status pet_takeout_request_status NOT NULL default 'undecided',
  created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
  resolved_at TIMESTAMP WITH TIME ZONE,
  PRIMARY KEY (pet_takeout_request_id),
  CONSTRAINT "CHECK_pet_takeout_request_when_resolved_has_timestamp" CHECK (
    (
      status = 'undecided' AND resolved_at is null
    ) OR (
      status != 'undecided' AND resolved_at is not null
    )
  ),

  CONSTRAINT "FK_pet_takeout_request.adopter"
    FOREIGN KEY (adopter_user_id)
      REFERENCES "user" (user_id),

  CONSTRAINT "FK_pet_takeout_request.employee_that_freed_pet"
    FOREIGN KEY (shelter_id, employee_user_id)
      REFERENCES employee_user_in_shelter (shelter_id, employee_user_id),

  CONSTRAINT "FK_pet_takeout_request.freed_pet"
    FOREIGN KEY (pet_instance_id, shelter_id)
      REFERENCES pet_instance (pet_instance_id, shelter_id)
);

CREATE UNIQUE INDEX "UQ_pet_takeout_request_can_be_resolved_only_once" ON pet_takeout_request (pet_instance_id)
WHERE status = 'approved';

CREATE UNIQUE INDEX "UQ_undecided_pet_and_adopter_pairs" ON pet_takeout_request (adopter_user_id, pet_instance_id)
WHERE status = 'undecided';


CREATE OR REPLACE FUNCTION validate_inserting_pet_takeout_request()
RETURNS TRIGGER AS $$
BEGIN
    -- should throw error during insert?
    -- 1 means Yes,
    -- 0 means No,
    -- AAerr means UQ_pet_takeout_request_can_be_resolved_only_once will throw error,
    -- auto_u means auto update
    --                            newRow.status
    -- existing_row_status\/  undecided approved rejected |
    --              undecided 0         0,auto_u 1        |
    --               approved 1         AAerr    1        |
    --               rejected 0         0,auto_u 1        |

    CASE NEW."status"
      WHEN 'rejected' THEN
        RAISE EXCEPTION 'Can''t insert rejected request. You can only insert undecided or approved requests'
          USING HINT = 'Exclude rejected requests from rows you are trying to insert';
      WHEN 'approved' THEN
        UPDATE pet_takeout_request
          SET status = 'rejected'
          WHERE "pet_instance_id" = NEW."pet_instance_id" AND "status" = 'undecided';
      WHEN 'undecided' THEN
        IF EXISTS (
          SELECT 1 FROM pet_takeout_request
          WHERE "pet_instance_id" = NEW."pet_instance_id"
          AND "status" = 'approved'
        ) THEN
          RAISE EXCEPTION 'Can''t insert rejected request. You can only insert undecided or approved requests'
            USING HINT = 'Exclude rejected requests from rows you are trying to insert';
        END IF;
    END CASE;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER before_insert_on_pet_takeout_request
BEFORE INSERT ON pet_takeout_request
FOR EACH ROW
EXECUTE FUNCTION validate_inserting_pet_takeout_request();




CREATE OR REPLACE FUNCTION validate_updating_status_in_pet_takeout_request()
RETURNS TRIGGER AS $$
BEGIN
    -- should throw error during update?
    -- 1 means Yes,
    -- 0 means No,
    -- nr means not reachable because of preliminary check
    --                                 newStatusOfExistingRow
    -- statusOfThisExistingRow\/  undecided approved rejected |
    --                  undecided nr        0        0        |
    --                   approved 1         nr       1        |
    --                   rejected 1         1        nr       |
    CASE
      WHEN NEW."status" = 'undecided' THEN /* (Undecided -> Undecided) not reachable because of preliminary check and other 2 bad options ((Approved/Rejected) -> Undecided) are left*/
        RAISE EXCEPTION 'Can''t set undecided status to pet takeout request which was already resolved (which has status approved or rejected)'
          USING HINT = 'Exclude resolved requests from rows you are trying to update';
      WHEN OLD."status" != 'undecided' THEN /* (Rejected -> Approved, Approved -> Rejected) */
        RAISE EXCEPTION 'Can''t change already resolved status of pet takeout request';
    END CASE;

    -- should throw error during update?
    -- 1 means Yes,
    -- 0 means No,
    -- nr means not reachable because of previous case checks
    -- AAerr means UQ_pet_takeout_request_can_be_resolved_only_once will throw error
    -- auto_u means auto update of other rows
    --                                 newStatusOfExistingRow
    -- statusOfAnotherExistingRow\/  undecided approved rejected |
    --                     undecided nr        0,auto_u 0        |
    --                      approved nr        AAerr    0        |
    --                      rejected nr        0,auto_u 0        |
    CASE NEW."status"
      WHEN 'approved' THEN
        UPDATE pet_takeout_request
          SET status = 'rejected'
          WHERE "pet_instance_id" = NEW."pet_instance_id" AND "status" = 'undecided';
      -- situation with attempt to set rejected status when there is already approved status on some other row is kinda strange
      -- because if there is approved status on some other row then there can't be undecided status on any row at all
      -- there can't be undecided status because when we tried to set approved status on some row we also automatically set rejected status on all other undecided rows
      -- we could throw an error here because of some strange shit is happening
      -- but actually additional setting of rejected status won't harm anything
      -- WHEN 'rejected' THEN
      --   IF EXISTS (
      --     SELECT 1 FROM pet_takeout_request
      --     WHERE "pet_instance_id" = NEW."pet_instance_id"
      --     AND "status" = 'approved'
      --   ) THEN
      --     RAISE EXCEPTION 'Can''t insert rejected request. You can only insert undecided or approved requests'
      --       USING HINT = 'Exclude rejected requests from rows you are trying to insert';
      --   END IF;
    END CASE;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER before_update_of_status_on_pet_takeout_request
BEFORE UPDATE OF "status" ON pet_takeout_request
FOR EACH ROW
WHEN (OLD.status IS DISTINCT FROM NEW.status)
EXECUTE FUNCTION validate_updating_status_in_pet_takeout_request();
