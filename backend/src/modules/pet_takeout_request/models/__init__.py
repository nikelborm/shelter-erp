from datetime import datetime
from pydantic import BaseModel
from src.db import PetTakeoutRequestStatusEnum


class PetTakeoutRequestWithoutId(BaseModel):
  adopterUserId: int
  shelterId: int
  employeeUserId: int
  petInstanceId: int
  status: PetTakeoutRequestStatusEnum
  createdAt: datetime
  resolvedAt: datetime | None

class PetTakeoutRequestPk(BaseModel):
  id: int

class PetTakeoutRequest(PetTakeoutRequestWithoutId, PetTakeoutRequestPk):
  pass
