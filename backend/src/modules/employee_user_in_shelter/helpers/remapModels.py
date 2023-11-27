from ..models import EmployeeUserInShelter, EmployeeUserInShelterWithoutId, EmployeeUserInShelterToCreate
from src.db import DBEmployeeUserInShelterWithoutId, DBEmployeeUserInShelter, DBEmployeeUserInShelterToInsert

def getDBEmployeeUserInShelterWithoutId(employee_user_in_shelter: EmployeeUserInShelterWithoutId) -> DBEmployeeUserInShelterWithoutId:
  return DBEmployeeUserInShelterWithoutId(
    is_active=employee_user_in_shelter.isActive,
    employed_at=employee_user_in_shelter.employedAt,
    employee_position=employee_user_in_shelter.employeePosition,
  )

def getDBEmployeeUserInShelterToInsert(employee_user_in_shelter: EmployeeUserInShelterToCreate) -> DBEmployeeUserInShelterToInsert:
  return DBEmployeeUserInShelterToInsert(
    is_active=employee_user_in_shelter.isActive,
    employed_at=employee_user_in_shelter.employedAt,
    employee_position=employee_user_in_shelter.employeePosition,
    shelter_id=employee_user_in_shelter.shelterId,
    employee_user_id=employee_user_in_shelter.employeeUserId,
  )

def getEmployeeUserInShelterWithoutId(db_employee_user_in_shelter: DBEmployeeUserInShelterWithoutId) -> EmployeeUserInShelterWithoutId:
  return EmployeeUserInShelterWithoutId(
    isActive=db_employee_user_in_shelter.is_active,
    employedAt=db_employee_user_in_shelter.employed_at,
    employeePosition=db_employee_user_in_shelter.employee_position,
  )

def getDBEmployeeUserInShelter(employee_user_in_shelter: EmployeeUserInShelter) -> DBEmployeeUserInShelter:
  return DBEmployeeUserInShelter(
    employee_user_id=employee_user_in_shelter.employeeUserId,
    shelter_id=employee_user_in_shelter.shelterId,
    **getDBEmployeeUserInShelterWithoutId(employee_user_in_shelter).model_dump(),
  )

def getEmployeeUserInShelter(db_employee_user_in_shelter: DBEmployeeUserInShelter) -> EmployeeUserInShelter:
  return EmployeeUserInShelter(
    employeeUserId=db_employee_user_in_shelter.employee_user_id,
    shelterId=db_employee_user_in_shelter.shelter_id,
    **getEmployeeUserInShelterWithoutId(db_employee_user_in_shelter).model_dump(),
  )
