from fastapi import HTTPException
from .models import EmployeeUser, EmployeeUserWithoutId
from .helpers import getDBEmployeeUserWithoutId, getEmployeeUser
from src.db import selectAllEmployeeUsers, insertEmployeeUser, selectEmployeeUserByPk, ZeroRowsReturnedException, DBEmployeeUserPk, deleteEmployeeUserByPk, updateEmployeeUserByPk, ZeroRowsAffectedException


async def getAllEmployeeUsers():
  db_employee_users = await selectAllEmployeeUsers()
  return [getEmployeeUser(db_employee_user) for db_employee_user in db_employee_users]

async def getOneEmployeeUserById(employee_user_id: int):
  try:
    db_employee_user = await selectEmployeeUserByPk(DBEmployeeUserPk(employee_user_id=employee_user_id))
  except ZeroRowsReturnedException:
    raise HTTPException(status_code=404, detail="EmployeeUser you tried to get was not found")

  return getEmployeeUser(db_employee_user)

async def createEmployeeUser(employee_user: EmployeeUserWithoutId) -> EmployeeUser:
  new_employee_user_id = await insertEmployeeUser(getDBEmployeeUserWithoutId(employee_user))
  return EmployeeUser(**employee_user.model_dump(), id=new_employee_user_id)

async def updateOneEmployeeUserById(employee_user_id: int, employee_user: EmployeeUserWithoutId):
  try:
    await updateEmployeeUserByPk(employee_user, DBEmployeeUserPk(employee_user_id=employee_user_id))
  except ZeroRowsAffectedException:
    raise HTTPException(status_code=404, detail="EmployeeUser you tried to update was not found")

async def deleteEmployeeUserById(employee_user_id: int):
  try:
    await deleteEmployeeUserByPk(DBEmployeeUserPk(employee_user_id=employee_user_id))
  except ZeroRowsAffectedException:
    raise HTTPException(status_code=404, detail="EmployeeUser you tried to update was not found")
