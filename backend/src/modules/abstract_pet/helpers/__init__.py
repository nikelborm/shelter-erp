from src.modules.abstract_pet.models import AbstractPet, AbstractPetWithoutId
from src.db.models import DBAbstractPetWithoutId, DBAbstractPet

def getDBAbstractPetWithoutId(abstract_pet: AbstractPetWithoutId) -> DBAbstractPetWithoutId:
  return DBAbstractPetWithoutId(
    parent_abstract_pet_id=abstract_pet.parentAbstractPetId,
    pet_class_name=abstract_pet.petClassName,
  )

def getAbstractPetWithoutId(db_abstract_pet: DBAbstractPetWithoutId) -> AbstractPetWithoutId:
  return AbstractPetWithoutId(
    parentAbstractPetId=db_abstract_pet.parent_abstract_pet_id,
    petClassName=db_abstract_pet.pet_class_name,
  )

def getDBAbstractPet(abstract_pet: AbstractPet) -> DBAbstractPet:
  return DBAbstractPet(
    abstract_pet_id=abstract_pet.id,
    **getDBAbstractPetWithoutId(abstract_pet).model_dump(),
  )

def getAbstractPet(db_abstract_pet: DBAbstractPet) -> AbstractPet:
  return AbstractPet(
    id=db_abstract_pet.abstract_pet_id,
    **getAbstractPetWithoutId(db_abstract_pet).model_dump(),
  )
