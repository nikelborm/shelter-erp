from pydantic import BaseModel, EmailStr

class EmployeeUserInShelterWithoutId(BaseModel):
  shelterId: int
  userId: int
  employedAt: str
  workEmail: EmailStr
  isActive: bool
  employeePosition: str

class EmployeeUserInShelter(EmployeeUserInShelterWithoutId):
  pass
