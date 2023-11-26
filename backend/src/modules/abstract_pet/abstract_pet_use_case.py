from fastapi import HTTPException
from .models import AbstractPet, AbstractPetWithoutId
from .helpers import getDBAbstractPetWithoutId, getAbstractPet
from src.db import selectAllAbstractPets, insertAbstractPet, selectAbstractPetByPk, ZeroRowsReturnedException, DBAbstractPetPk, deleteAbstractPetByPk, updateAbstractPetByPk, ZeroRowsAffectedException


async def getAllAbstractPets():
  db_abstract_pets = await selectAllAbstractPets()
  return [getAbstractPet(db_abstract_pet) for db_abstract_pet in db_abstract_pets]

async def getOneAbstractPetById(abstract_pet_id: int):
  try:
    db_abstract_pet = await selectAbstractPetByPk(DBAbstractPetPk(abstract_pet_id=abstract_pet_id))
  except ZeroRowsReturnedException:
    raise HTTPException(status_code=404, detail="AbstractPet you tried to get was not found")

  return getAbstractPet(db_abstract_pet)

async def createAbstractPet(abstract_pet: AbstractPetWithoutId) -> AbstractPet:
  new_abstract_pet_id = await insertAbstractPet(getDBAbstractPetWithoutId(abstract_pet))
  return AbstractPet(**abstract_pet.model_dump(), id=new_abstract_pet_id)

async def updateOneAbstractPetById(abstract_pet_id: int, abstract_pet: AbstractPetWithoutId):
  try:
    await updateAbstractPetByPk(abstract_pet, DBAbstractPetPk(abstract_pet_id=abstract_pet_id))
  except ZeroRowsAffectedException:
    raise HTTPException(status_code=404, detail="AbstractPet you tried to update was not found")

async def deleteAbstractPetById(abstract_pet_id: int):
  try:
    await deleteAbstractPetByPk(DBAbstractPetPk(abstract_pet_id=abstract_pet_id))
  except ZeroRowsAffectedException:
    raise HTTPException(status_code=404, detail="AbstractPet you tried to update was not found")
