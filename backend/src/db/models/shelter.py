from pydantic import BaseModel

class DBShelterWithoutId(BaseModel):
  name: str
  address: str

class DBShelter(DBShelterWithoutId):
  shelter_id: int
