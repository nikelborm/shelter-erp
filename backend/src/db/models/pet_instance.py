from pydantic import BaseModel
from datetime import datetime

class DBPetInstanceWithoutId(BaseModel):
  shelter_id: int
  abstract_pet_id: int
  was_brought_at: datetime
  name: str

class DBPetInstancePk(BaseModel):
  pet_instance_id: int

class DBPetInstance(DBPetInstanceWithoutId, DBPetInstancePk):
  pass
