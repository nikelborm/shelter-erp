from pydantic import BaseModel

class DBPetInstanceWithoutIdToInsert(BaseModel):
  shelter_id: int
  abstract_pet_id: int

class DBPetInstanceWithoutId(BaseModel):
  shelter_id: int
  abstract_pet_id: int
  was_brought_at: str

class DBPetInstance(DBPetInstanceWithoutId):
  pet_instance_id: int
