from pydantic import BaseModel, EmailStr

class EmployeeUserWithoutId(BaseModel):
  passwordSalt: str
  passwordHash: str
  workEmail: EmailStr

class EmployeeUserPk(BaseModel):
  id: int

class EmployeeUser(EmployeeUserWithoutId, EmployeeUserPk):
  pass
