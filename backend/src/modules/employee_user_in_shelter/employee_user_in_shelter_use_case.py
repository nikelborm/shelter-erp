from fastapi import HTTPException
from .models import EmployeeUserInShelter, EmployeeUserInShelterWithoutId, EmployeeUserInShelterToCreate
from .helpers import getDBEmployeeUserInShelterWithoutId, getEmployeeUserInShelter, getDBEmployeeUserInShelterToInsert
from src.db import selectAllEmployeeUserInShelters, insertEmployeeUserInShelter, selectEmployeeUserInShelterByPk, ZeroRowsReturnedException, DBEmployeeUserInShelterPk, deleteEmployeeUserInShelterByPk, updateEmployeeUserInShelterByPk, ZeroRowsAffectedException, EMPLOYEE_USER_IN_SHELTER_CNS


async def getAllEmployeeUserInShelters():
  db_employee_user_in_shelters = await selectAllEmployeeUserInShelters()
  return [getEmployeeUserInShelter(db_employee_user_in_shelter) for db_employee_user_in_shelter in db_employee_user_in_shelters]

async def getOneEmployeeUserInShelterById(employee_user_id: int, shelter_id: int):
  try:
    db_employee_user_in_shelter = await selectEmployeeUserInShelterByPk(
      DBEmployeeUserInShelterPk(
        employee_user_id=employee_user_id,
        shelter_id=shelter_id
      ))
  except ZeroRowsReturnedException:
    raise HTTPException(status_code=404, detail="EmployeeUserInShelter you tried to get was not found")

  return getEmployeeUserInShelter(db_employee_user_in_shelter)

async def createEmployeeUserInShelter(employee_user_in_shelter: EmployeeUserInShelterToCreate) -> EmployeeUserInShelter:
  columnsWithDefaults = set()
  model_to_insert = getDBEmployeeUserInShelterToInsert(employee_user_in_shelter)

  if employee_user_in_shelter.isActive is None:
    delattr(model_to_insert, EMPLOYEE_USER_IN_SHELTER_CNS.IS_ACTIVE)
    columnsWithDefaults.add(EMPLOYEE_USER_IN_SHELTER_CNS.IS_ACTIVE)

  if employee_user_in_shelter.employedAt is None:
    delattr(model_to_insert, EMPLOYEE_USER_IN_SHELTER_CNS.EMPLOYED_AT)
    columnsWithDefaults.add(EMPLOYEE_USER_IN_SHELTER_CNS.EMPLOYED_AT)

  employee_user_in_shelter_record = await insertEmployeeUserInShelter(model_to_insert,frozenset(columnsWithDefaults))
  return EmployeeUserInShelter(
    **employee_user_in_shelter.model_dump(),
    isActive=employee_user_in_shelter_record.get(EMPLOYEE_USER_IN_SHELTER_CNS.IS_ACTIVE, employee_user_in_shelter.isActive),
    employedAt=employee_user_in_shelter_record.get(EMPLOYEE_USER_IN_SHELTER_CNS.EMPLOYED_AT, employee_user_in_shelter.employedAt),
  )

async def updateOneEmployeeUserInShelterById(employee_user_id: int, shelter_id: int, employee_user_in_shelter: EmployeeUserInShelterWithoutId):
  try:
    await updateEmployeeUserInShelterByPk(
      employee_user_in_shelter,
      DBEmployeeUserInShelterPk(
        employee_user_id=employee_user_id,
        shelter_id=shelter_id
      )
    )
  except ZeroRowsAffectedException:
    raise HTTPException(status_code=404, detail="EmployeeUserInShelter you tried to update was not found")

async def deleteEmployeeUserInShelterById(employee_user_id: int, shelter_id: int):
  try:
    await deleteEmployeeUserInShelterByPk(
      DBEmployeeUserInShelterPk(
        employee_user_id=employee_user_id,
        shelter_id=shelter_id
      )
    )
  except ZeroRowsAffectedException:
    raise HTTPException(status_code=404, detail="EmployeeUserInShelter you tried to update was not found")
