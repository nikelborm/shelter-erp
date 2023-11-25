from pydantic import BaseModel

class ShelterWithoutId(BaseModel):
  name: str
  address: str

class Shelter(ShelterWithoutId):
  id: int
