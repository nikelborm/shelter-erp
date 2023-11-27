from ..models import EmployeeUser, EmployeeUserWithoutId
from src.db import DBEmployeeUserWithoutId, DBEmployeeUser

def getDBEmployeeUserWithoutId(employee_user: EmployeeUserWithoutId) -> DBEmployeeUserWithoutId:
  return DBEmployeeUserWithoutId(
    password_salt=employee_user.passwordSalt,
    password_hash=employee_user.passwordHash,
    work_email=employee_user.workEmail,
  )

def getEmployeeUserWithoutId(db_employee_user: DBEmployeeUserWithoutId) -> EmployeeUserWithoutId:
  return EmployeeUserWithoutId(
    passwordSalt=db_employee_user.password_salt,
    passwordHash=db_employee_user.password_hash,
    workEmail=db_employee_user.work_email,
  )

def getDBEmployeeUser(employee_user: EmployeeUser) -> DBEmployeeUser:
  return DBEmployeeUser(
    employee_user_id=employee_user.id,
    **getDBEmployeeUserWithoutId(employee_user).model_dump(),
  )

def getEmployeeUser(db_employee_user: DBEmployeeUser) -> EmployeeUser:
  return EmployeeUser(
    id=db_employee_user.employee_user_id,
    **getEmployeeUserWithoutId(db_employee_user).model_dump(),
  )
