from enum import StrEnum
from pydantic import BaseModel
from src.config import DATABASE_SCHEMA
from .tools import DbTable
from .models import DBUser, DBShelter, DBPetInstance, DBAbstractPet, DBUserPk, DBShelterPk, DBPetInstancePk, DBAbstractPetPk

class SHELTER_CNS(StrEnum):
  SHELTER_ID = 'shelter_id'
  ADDRESS = 'address'
  NAME = 'name'

ShelterTable = DbTable(
  table_name=f'{DATABASE_SCHEMA}.shelter',
  pydanticModelForSelectStar=DBShelter,
  columns=SHELTER_CNS,
  always_generated_columns=frozenset({SHELTER_CNS.SHELTER_ID}),
  pydanticPkModel=DBShelterPk,
)

class USER_CNS(StrEnum):
  USER_ID = 'user_id'
  FIRST_NAME = 'first_name'
  SECOND_NAME = 'second_name'
  EMAIL = 'email'
  PHONE = 'phone'

UserTable = DbTable(
  table_name=f'{DATABASE_SCHEMA}."user"',
  pydanticModelForSelectStar=DBUser,
  columns=USER_CNS,
  always_generated_columns=frozenset({USER_CNS.USER_ID}),
  pydanticPkModel=DBUserPk
)

class EMPLOYEE_USER_CNS(StrEnum):
  EMPLOYEE_USER_ID = 'employee_user_id'
  PASSWORD_SALT = 'password_salt'
  PASSWORD_HASH = 'password_hash'
  WORK_EMAIL = 'work_email'

EmployeeUserTable = DbTable(
  table_name=f'{DATABASE_SCHEMA}.employee_user',
  pydanticModelForSelectStar=BaseModel,
  pydanticPkModel=BaseModel, # TODO change to normal model
  columns=EMPLOYEE_USER_CNS,
  readonly_columns=frozenset({EMPLOYEE_USER_CNS.EMPLOYEE_USER_ID}),
)

class EMPLOYEE_USER_IN_SHELTER_CNS(StrEnum):
  EMPLOYEE_USER_ID = 'employee_user_id'
  SHELTER_ID = 'shelter_id'
  EMPLOYED_AT = 'employed_at'
  IS_ACTIVE = 'is_active'
  EMPLOYEE_POSITION = 'employee_position'

EmployeeUserInShelterTable = DbTable(
  table_name=f'{DATABASE_SCHEMA}.employee_user_in_shelter',
  pydanticModelForSelectStar=BaseModel,
  pydanticPkModel=BaseModel, # TODO change to normal model
  # pk_columns=frozenset({EMPLOYEE_USER_CNS.USER_ID, EMPLOYEE_USER_CNS.SHELTER_ID}),
  columns=EMPLOYEE_USER_IN_SHELTER_CNS,
  columns_with_defaults=frozenset({
    EMPLOYEE_USER_IN_SHELTER_CNS.EMPLOYED_AT,
    EMPLOYEE_USER_IN_SHELTER_CNS.IS_ACTIVE}),
  readonly_columns=frozenset({EMPLOYEE_USER_IN_SHELTER_CNS.EMPLOYEE_USER_ID}),
)


class ABSTRACT_PET_CNS(StrEnum):
  ABSTRACT_PET_ID = 'abstract_pet_id'
  PARENT_ABSTRACT_PET_ID = 'parent_abstract_pet_id'
  PET_CLASS_NAME = 'pet_class_name'

AbstractPetTable = DbTable(
  table_name=f'{DATABASE_SCHEMA}.abstract_pet',
  pydanticModelForSelectStar=DBAbstractPet,
  columns=ABSTRACT_PET_CNS,
  always_generated_columns=frozenset({ABSTRACT_PET_CNS.ABSTRACT_PET_ID}),
  pydanticPkModel=DBAbstractPetPk,
  columns_with_defaults=frozenset({ABSTRACT_PET_CNS.PARENT_ABSTRACT_PET_ID}),
)


class PET_INSTANCE_CNS(StrEnum):
  PET_INSTANCE_ID = 'pet_instance_id'
  ABSTRACT_PET_ID = 'abstract_pet_id'
  SHELTER_ID = 'shelter_id'
  WAS_BROUGHT_AT = 'was_brought_at'
  NAME = 'name'

PetInstanceTable = DbTable(
  table_name=f'{DATABASE_SCHEMA}.pet_instance',
  pydanticModelForSelectStar=DBPetInstance,
  columns=PET_INSTANCE_CNS,
  always_generated_columns=frozenset({PET_INSTANCE_CNS.PET_INSTANCE_ID}),
  pydanticPkModel=DBPetInstancePk,
  columns_with_defaults=frozenset({PET_INSTANCE_CNS.WAS_BROUGHT_AT}),
)

class PET_TAKEOUT_REQUEST_CNS(StrEnum):
  PET_TAKEOUT_REQUEST_ID = 'pet_takeout_request_id'
  ADOPTER_USER_ID = 'adopter_user_id'
  EMPLOYEE_USER_ID = 'employee_user_id'
  SHELTER_ID = 'shelter_id'
  PET_INSTANCE_ID = 'pet_instance_id'
  STATUS = 'status'
  CREATED_AT = 'created_at'
  RESOLVED_AT = 'resolved_at'

PetTakeoutRequestTable = DbTable(
  table_name=f'{DATABASE_SCHEMA}.pet_takeout_request',
  pydanticModelForSelectStar=BaseModel,
  pydanticPkModel=BaseModel, # TODO change to normal model
  columns=PET_TAKEOUT_REQUEST_CNS,
  always_generated_columns=frozenset({PET_TAKEOUT_REQUEST_CNS.PET_TAKEOUT_REQUEST_ID}),
  columns_with_defaults=frozenset({
    PET_TAKEOUT_REQUEST_CNS.STATUS,
    PET_TAKEOUT_REQUEST_CNS.CREATED_AT,
    PET_TAKEOUT_REQUEST_CNS.RESOLVED_AT}),
  readonly_columns=frozenset({
    PET_TAKEOUT_REQUEST_CNS.ADOPTER_USER_ID,
    PET_TAKEOUT_REQUEST_CNS.EMPLOYEE_USER_ID,
    PET_TAKEOUT_REQUEST_CNS.SHELTER_ID,
    PET_TAKEOUT_REQUEST_CNS.PET_INSTANCE_ID,
    PET_TAKEOUT_REQUEST_CNS.CREATED_AT,
  }),
)
