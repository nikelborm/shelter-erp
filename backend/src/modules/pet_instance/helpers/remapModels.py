from ..models import PetInstance, PetInstanceWithoutId, PetInstanceToCreate
from src.db import DBPetInstanceToInsert, DBPetInstance, DBPetInstanceWithoutId

def getDBPetInstanceWithoutId(pet_instance: PetInstanceWithoutId) -> DBPetInstanceWithoutId:
  return DBPetInstanceWithoutId(
    shelter_id=pet_instance.shelterId,
    abstract_pet_id=pet_instance.abstractPetId,
    was_brought_at=pet_instance.wasBroughtAt,
    name=pet_instance.name,
  )

def getDBPetInstanceToInsert(pet_instance: PetInstanceToCreate) -> DBPetInstanceToInsert:
  return DBPetInstanceToInsert(
    shelter_id=pet_instance.shelterId,
    abstract_pet_id=pet_instance.abstractPetId,
    was_brought_at=pet_instance.wasBroughtAt,
    name=pet_instance.name,
  )

def getPetInstanceWithoutId(db_pet_instance: DBPetInstanceWithoutId) -> PetInstanceWithoutId:
  return PetInstanceWithoutId(
    shelterId=db_pet_instance.shelter_id,
    abstractPetId=db_pet_instance.abstract_pet_id,
    wasBroughtAt=db_pet_instance.was_brought_at,
    name=db_pet_instance.name,
  )

def getDBPetInstance(pet_instance: PetInstance) -> DBPetInstance:
  return DBPetInstance(
    **getDBPetInstanceWithoutId(pet_instance).model_dump(),
    pet_instance_id=pet_instance.id,
  )

def getPetInstance(db_pet_instance: DBPetInstance) -> PetInstance:
  return PetInstance(
    **getPetInstanceWithoutId(db_pet_instance).model_dump(),
    id=db_pet_instance.pet_instance_id,
  )
