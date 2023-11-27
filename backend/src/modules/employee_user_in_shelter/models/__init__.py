from datetime import datetime
from pydantic import BaseModel, EmailStr

class EmployeeUserInShelterWithoutId(BaseModel):
  isActive: bool
  employedAt: datetime
  employeePosition: str

class EmployeeUserInShelterToCreate(BaseModel):
  isActive: bool | None
  employedAt: datetime | None
  employeePosition: str
  employeeUserId: int
  shelterId: int

class EmployeeUserInShelterPk(BaseModel):
  employeeUserId: int
  shelterId: int

class EmployeeUserInShelter(EmployeeUserInShelterWithoutId, EmployeeUserInShelterPk):
  pass
