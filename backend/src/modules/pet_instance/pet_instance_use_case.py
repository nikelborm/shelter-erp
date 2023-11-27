from fastapi import HTTPException
from src.db import selectAllPetInstances, insertPetInstance, selectPetInstanceByPk, ZeroRowsReturnedException, DBPetInstancePk, deletePetInstanceByPk, updatePetInstanceByPk, ZeroRowsAffectedException, PET_INSTANCE_CNS
from .models import PetInstance, PetInstanceWithoutId, PetInstanceToCreate
from .helpers import getPetInstance, getDBPetInstanceToInsert


async def getAllPetInstances():
  db_pet_instances = await selectAllPetInstances()
  return [getPetInstance(db_pet_instance) for db_pet_instance in db_pet_instances]

async def getOnePetInstanceById(pet_instance_id: int):
  try:
    db_pet_instance = await selectPetInstanceByPk(DBPetInstancePk(pet_instance_id=pet_instance_id))
  except ZeroRowsReturnedException:
    raise HTTPException(status_code=404, detail="PetInstance you tried to get was not found")

  return getPetInstance(db_pet_instance)

async def createPetInstance(pet_instance: PetInstanceToCreate) -> PetInstance:
  columnsWithDefaults = set()
  model_to_insert = getDBPetInstanceToInsert(pet_instance)
  if pet_instance.wasBroughtAt is None:
    delattr(model_to_insert, PET_INSTANCE_CNS.WAS_BROUGHT_AT)
    columnsWithDefaults.add(PET_INSTANCE_CNS.WAS_BROUGHT_AT)
  pet_instance_record = await insertPetInstance(model_to_insert)

  return PetInstance(
    **pet_instance.model_dump(),
    id=pet_instance_record[PET_INSTANCE_CNS.PET_INSTANCE_ID],
    wasBroughtAt=pet_instance_record.get(PET_INSTANCE_CNS.WAS_BROUGHT_AT, pet_instance.wasBroughtAt),
  )

async def updateOnePetInstanceById(pet_instance_id: int, pet_instance: PetInstanceWithoutId):
  try:
    await updatePetInstanceByPk(pet_instance, DBPetInstancePk(pet_instance_id=pet_instance_id))
  except ZeroRowsAffectedException:
    raise HTTPException(status_code=404, detail="PetInstance you tried to update was not found")

async def deletePetInstanceById(pet_instance_id: int):
  try:
    await deletePetInstanceByPk(DBPetInstancePk(pet_instance_id=pet_instance_id))
  except ZeroRowsAffectedException:
    raise HTTPException(status_code=404, detail="PetInstance you tried to update was not found")
