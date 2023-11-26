from ..models import Shelter, ShelterWithoutId
from src.db import DBShelterWithoutId, DBShelter

def getDBShelterWithoutId(shelter: ShelterWithoutId) -> DBShelterWithoutId:
  return DBShelterWithoutId(
    name=shelter.name,
    address=shelter.address,
  )

def getShelterWithoutId(db_shelter: DBShelterWithoutId) -> ShelterWithoutId:
  return ShelterWithoutId(
    name=db_shelter.name,
    address=db_shelter.address,
  )

def getDBShelter(shelter: Shelter) -> DBShelter:
  return DBShelter(
    shelter_id=shelter.id,
    **getDBShelterWithoutId(shelter).model_dump(),
  )

def getShelter(db_shelter: DBShelter) -> Shelter:
  return Shelter(
    id=db_shelter.shelter_id,
    **getShelterWithoutId(db_shelter).model_dump(),
  )
