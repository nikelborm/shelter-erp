from pydantic import BaseModel

class AbstractPetWithoutId(BaseModel):
  parent_abstract_pet_id: int
  pet_class_name: str

class AbstractPet(AbstractPetWithoutId):
  id: int
