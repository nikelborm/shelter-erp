from pydantic import BaseModel, EmailStr

class EmployeeUserWithoutId(BaseModel):
  shelterId: int
  userId: int
  employedAt: str
  workEmail: EmailStr
  isActive: bool
  employeePosition: str

class EmployeeUser(EmployeeUserWithoutId):
  pass
