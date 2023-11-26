from datetime import datetime
from pydantic import BaseModel, EmailStr

class DBEmployeeUserInShelterWithoutId(BaseModel):
  is_active: bool
  employed_at: datetime
  employee_position: str

class DBEmployeeUserInShelterPk(BaseModel):
  employee_user_id: int
  shelter_id: int

class DBEmployeeUserInShelter(DBEmployeeUserInShelterWithoutId, DBEmployeeUserInShelterPk):
  pass
