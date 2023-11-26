from enum import StrEnum
from datetime import datetime
from pydantic import BaseModel

class PetTakeoutRequestStatusEnum(StrEnum):
  UNDECIDED = 'undecided'
  APPROVED = 'approved'
  REJECTED = 'rejected'

class DBPetTakeoutRequestWithoutId(BaseModel):
  adopter_user_id: int
  shelter_id: int
  employee_user_id: int
  pet_instance_id: int
  status: PetTakeoutRequestStatusEnum
  created_at: datetime
  resolved_at: datetime | None

class DBPetTakeoutRequestPk(BaseModel):
  pet_takeout_request_id: int

class DBPetTakeoutRequest(DBPetTakeoutRequestWithoutId, DBPetTakeoutRequestPk):
  pass
