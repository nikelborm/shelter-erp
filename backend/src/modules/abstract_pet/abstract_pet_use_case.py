from fastapi import HTTPException
from src.db import selectAllAbstractPets, insertAbstractPet, selectAbstractPetByPk, ZeroRowsReturnedException, DBAbstractPetPk, deleteAbstractPetByPk, updateAbstractPetByPk, ZeroRowsAffectedException, ABSTRACT_PET_CNS
from .models import AbstractPet, AbstractPetWithoutId
from .helpers import getDBAbstractPetWithoutId, getAbstractPet


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
  columnsWithDefaults = set()
  model_to_insert = getDBAbstractPetWithoutId(abstract_pet)

  if abstract_pet.parentAbstractPetId is None:
    delattr(model_to_insert, ABSTRACT_PET_CNS.PARENT_ABSTRACT_PET_ID)
    columnsWithDefaults.add(ABSTRACT_PET_CNS.PARENT_ABSTRACT_PET_ID)

  abstract_pet_record = await insertAbstractPet(
    model_to_insert,
    frozenset(columnsWithDefaults)
  )
  return AbstractPet(
    **abstract_pet.model_dump(),
    id=abstract_pet_record[ABSTRACT_PET_CNS.ABSTRACT_PET_ID],
    parentAbstractPetId=abstract_pet_record.get(ABSTRACT_PET_CNS.PARENT_ABSTRACT_PET_ID, None)
  )

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
