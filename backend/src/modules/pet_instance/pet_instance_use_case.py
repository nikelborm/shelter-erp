from fastapi import HTTPException

from .models import PetInstance, PetInstanceWithoutId
from src.db.queries import selectAllPetInstances, insertPetInstance, selectPetInstanceById
from src.db.errors import ReturnedZeroRowsException
from src.db.models import DBPetInstanceWithoutIdToInsert


async def getAllPetInstances():
  db_pet_instances = await selectAllPetInstances()
  return [PetInstance(
    id=db_pet_instance.pet_instance_id,
    shelterId=db_pet_instance.shelter_id,
    abstractPetId=db_pet_instance.abstract_pet_id,
    wasBroughtAt=db_pet_instance.was_brought_at,
  ) for db_pet_instance in db_pet_instances]

async def getOnePetInstanceById(pet_instance_id: int):
  try:
    db_pet_instance = await selectPetInstanceById(pet_instance_id)
  except ReturnedZeroRowsException:
    raise HTTPException(status_code=404, detail="PetInstance not found")

  return PetInstance(
    id=db_pet_instance.pet_instance_id,
    shelterId=db_pet_instance.shelter_id,
    abstractPetId=db_pet_instance.abstract_pet_id,
    wasBroughtAt=db_pet_instance.was_brought_at,
  )

async def createPetInstance(pet_instance: PetInstanceWithoutId) -> PetInstance:
  new_pet_instance_id, was_brought_at = await insertPetInstance(DBPetInstanceWithoutIdToInsert(
    shelter_id=pet_instance.shelterId,
    abstract_pet_id=pet_instance.abstractPetId,
    # was_brought_at=pet_instance.wasBroughtAt,
  ))
  return PetInstance(**pet_instance.model_dump(), id=new_pet_instance_id, wasBroughtAt=was_brought_at)

async def updateOnePetInstanceById(pet_instance_id: int, pet_instance: PetInstanceWithoutId):
  pass

async def deletePetInstanceById(pet_instance_id: int):
  pass
