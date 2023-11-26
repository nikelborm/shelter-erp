from pydantic import BaseModel, EmailStr

class DBEmployeeUserWithoutId(BaseModel):
  password_salt: str
  password_hash: str
  work_email: EmailStr

class DBEmployeeUserPk(BaseModel):
  employee_user_id: int

class DBEmployeeUser(DBEmployeeUserWithoutId, DBEmployeeUserPk):
  pass
