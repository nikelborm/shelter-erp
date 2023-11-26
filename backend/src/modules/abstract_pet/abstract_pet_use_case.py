from fastapi import HTTPException
from .models import AbstractPet, AbstractPetWithoutId
from .helpers import getDBAbstractPetWithoutId, getAbstractPet
from src.db import selectAllAbstractPets, insertAbstractPet, selectAbstractPetByPk, ReturnedZeroRowsException, ABSTRACT_PET_CNS


async def getAllAbstractPets():
  db_abstract_pets = await selectAllAbstractPets()
  return [getAbstractPet(db_abstract_pet) for db_abstract_pet in db_abstract_pets]

async def getOneAbstractPetById(abstract_pet_id: int):
  try:
    db_abstract_pet = await selectAbstractPetByPk({ ABSTRACT_PET_CNS.ABSTRACT_PET_ID: abstract_pet_id })
  except ReturnedZeroRowsException:
    raise HTTPException(status_code=404, detail="AbstractPet not found")

  return getAbstractPet(db_abstract_pet)

async def createAbstractPet(abstract_pet: AbstractPetWithoutId) -> AbstractPet:
  new_abstract_pet_id = await insertAbstractPet(getDBAbstractPetWithoutId(abstract_pet))
  return AbstractPet(**abstract_pet.model_dump(), id=new_abstract_pet_id)

async def updateOneAbstractPetById(abstract_pet_id: int, abstract_pet: AbstractPetWithoutId):
  pass

async def deleteAbstractPetById(abstract_pet_id: int):
  pass
