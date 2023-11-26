from fastapi import HTTPException
from .models import PetInstance, PetInstanceWithoutId
from .helpers import getDBPetInstanceWithoutId, getPetInstance
from src.db import selectAllPetInstances, insertPetInstance, selectPetInstanceByPk, ZeroRowsReturnedException, DBPetInstancePk, deletePetInstanceByPk, updatePetInstanceByPk, ZeroRowsAffectedException


async def getAllPetInstances():
  db_pet_instances = await selectAllPetInstances()
  return [getPetInstance(db_pet_instance) for db_pet_instance in db_pet_instances]

async def getOnePetInstanceById(pet_instance_id: int):
  try:
    db_pet_instance = await selectPetInstanceByPk(DBPetInstancePk(pet_instance_id=pet_instance_id))
  except ZeroRowsReturnedException:
    raise HTTPException(status_code=404, detail="PetInstance you tried to get was not found")

  return getPetInstance(db_pet_instance)

async def createPetInstance(pet_instance: PetInstanceWithoutId) -> PetInstance:
  new_pet_instance_id = await insertPetInstance(getDBPetInstanceWithoutId(pet_instance))
  return PetInstance(**pet_instance.model_dump(), id=new_pet_instance_id)

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
