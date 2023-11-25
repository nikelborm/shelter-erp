from pydantic import BaseModel, EmailStr

class EmployeeWithoutId(BaseModel):
  shelterId: int
  userId: int
  employedAt: str
  workEmail: EmailStr
  isActive: bool
  employeePosition: str

class Employee(EmployeeWithoutId):
  pass
