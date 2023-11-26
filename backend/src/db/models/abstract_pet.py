from pydantic import BaseModel

class DBAbstractPetWithoutId(BaseModel):
  parent_abstract_pet_id: int | None
  pet_class_name: str

class DBAbstractPetPk(BaseModel):
  abstract_pet_id: int

class DBAbstractPet(DBAbstractPetWithoutId, DBAbstractPetPk):
  pass
