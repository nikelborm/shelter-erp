from pydantic import BaseModel

class PetInstanceWithoutId(BaseModel):
  shelterId: int
  abstractPetId: int
  wasBroughtAt: str

class PetInstance(PetInstanceWithoutId):
  id: int
