from pydantic import BaseModel

class DBAbstractPetWithoutId(BaseModel):
  parent_abstract_pet_id: int | None
  pet_class_name: str

class DBAbstractPet(DBAbstractPetWithoutId):
  abstract_pet_id: int
