from fastapi import HTTPException

from src.config.tables_column_names import PET_INSTANCE_CNS
from .models import PetInstance, PetInstanceWithoutId
from .helpers import getDBPetInstanceWithoutId, getPetInstance
from src.db.queries import selectAllPetInstances, insertPetInstance, selectPetInstanceByPk
from src.db.errors import ReturnedZeroRowsException

async def getAllPetInstances():
  db_pet_instances = await selectAllPetInstances()
  return [getPetInstance(db_pet_instance) for db_pet_instance in db_pet_instances]

async def getOnePetInstanceById(pet_instance_id: int):
  try:
    db_pet_instance = await selectPetInstanceByPk({ PET_INSTANCE_CNS.PET_INSTANCE_ID: pet_instance_id })
  except ReturnedZeroRowsException:
    raise HTTPException(status_code=404, detail="PetInstance not found")

  return getPetInstance(db_pet_instance)

async def createPetInstance(pet_instance: PetInstanceWithoutId) -> PetInstance:
  new_pet_instance_id = await insertPetInstance(getDBPetInstanceWithoutId(pet_instance))
  return PetInstance(**pet_instance.model_dump(), id=new_pet_instance_id)

async def updateOnePetInstanceById(pet_instance_id: int, pet_instance: PetInstanceWithoutId):
  pass

async def deletePetInstanceById(pet_instance_id: int):
  pass
