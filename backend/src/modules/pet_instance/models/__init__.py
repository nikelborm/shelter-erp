from datetime import datetime
from pydantic import BaseModel

class PetInstanceWithoutId(BaseModel):
  shelterId: int
  abstractPetId: int
  wasBroughtAt: datetime
  name: str

class PetInstance(PetInstanceWithoutId):
  id: int
