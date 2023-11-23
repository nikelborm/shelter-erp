-- DROP TABLE IF EXISTS shelter, "user", employee, abstract_pet, pet_instance, pet_takeout_request CASCADE;
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

CREATE TABLE employee (
  shelter_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  employed_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
  password_salt char(32) NOT NULL,
  password_hash char(32) NOT NULL,
  work_email TEXT NOT NULL,
  active BOOLEAN NOT NULL DEFAULT TRUE,
  employee_position TEXT NOT NULL,
  PRIMARY KEY (shelter_id, user_id),
  CONSTRAINT "UQ_employee_work_email" UNIQUE (work_email),

  CONSTRAINT "FK_employee.shelter_id"
    FOREIGN KEY (shelter_id)
      REFERENCES shelter (shelter_id),

  CONSTRAINT "FK_employee.user_id"
    FOREIGN KEY (user_id)
      REFERENCES "user" (user_id)
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
  employee_user_id INTEGER NOT NULL,
  shelter_id INTEGER NOT NULL,
  pet_instance_id INTEGER NOT NULL,
  status pet_takeout_request_status NOT NULL default 'undecided',
  created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
  resolved_at TIMESTAMP WITH TIME ZONE DEFAULT NULL,
  PRIMARY KEY (pet_takeout_request_id),
  CONSTRAINT "CHECK_pet_takeout_request_when_resolved_has_timestamp" CHECK (
    (
      status = 'undecided' AND resolved_at is null
    ) OR (
      status != 'undecided' AND resolved_at is not null
    )
  ),
  -- EXCLUDE USING gist...

  CONSTRAINT "FK_pet_takeout_request.adopter"
    FOREIGN KEY (adopter_user_id)
      REFERENCES "user" (user_id),

  CONSTRAINT "FK_pet_takeout_request.employee_that_freed_pet"
    FOREIGN KEY (employee_user_id, shelter_id)
      REFERENCES employee (user_id, shelter_id),

  CONSTRAINT "FK_pet_takeout_request.freed_pet"
    FOREIGN KEY (pet_instance_id, shelter_id)
      REFERENCES pet_instance (pet_instance_id, shelter_id)
);

CREATE INDEX "UQ_pet_takeout_request_can_be_resolved_only_once" ON pet_takeout_request (pet_instance_id)
WHERE status = 'approved';
