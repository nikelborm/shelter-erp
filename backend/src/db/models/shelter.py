from pydantic import BaseModel

class DBShelterWithoutId(BaseModel):
  name: str
  address: str

class DBShelterPk(BaseModel):
  shelter_id: int

class DBShelter(DBShelterWithoutId, DBShelterPk):
  pass
