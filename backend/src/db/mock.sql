BEGIN;

INSERT INTO "shelter" ("name", "address")
VALUES
  ('Happy Paws Shelter', '123 Main Street, Anytown, USA'),
  ('Furry Friends Haven', '456 Oak Avenue, Sometown, USA'),
  ('Whiskers and Tails Rescue', '789 Elm Road, Othertown, USA');

INSERT INTO "user" ("first_name", "second_name", "email", "phone")
VALUES
  ('John', 'Doe', 'john@example.com', '123-456-7890'),
  ('Jane', 'Smith', 'jane@example.com', '987-654-3210'),
  ('Alex', 'Johnson', 'alex@example.com', '555-555-5555');

INSERT INTO "employee" ("shelter_id", "user_id", "password_salt", "password_hash", "work_email", "employee_position")
VALUES
  (1, 1, 'salt1', 'hash1', 'john@happypaws.com', 'Manager'),
  (2, 2, 'salt2', 'hash2', 'jane@furryfriends.com', 'Supervisor'),
  (3, 2, 'salt3', 'hash3', 'alex@whiskersandtails.com', 'Caregiver');

INSERT INTO "abstract_pet" ("parent_abstract_pet_id", "pet_class_name")
VALUES
  (NULL, 'Dog'),
  (1, 'Shepherd'),
  (NULL, 'Cat'),
  (3, 'Siamese');

INSERT INTO "pet_instance" ("shelter_id", "abstract_pet_id", "name")
VALUES
  (1, 1, 'Buddy'),
  (1, 2, 'Rex'),
  (3, 3, 'Whiskers'),
  (3, 4, 'Mittens');

INSERT INTO "pet_takeout_request" ("adopter_user_id", "employee_user_id", "shelter_id", "pet_instance_id", "status", "created_at", "resolved_at")
VALUES
  (1, 1, 1, 1, 'approved', '2023-11-23 10:00:00', '2023-11-23 11:00:00'),
  (2, 2, 3, 3, 'rejected', '2023-11-22 09:00:00', NULL);

COMMIT;
