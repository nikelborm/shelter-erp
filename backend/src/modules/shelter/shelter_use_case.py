from fastapi import HTTPException
from .models import Shelter, ShelterWithoutId
from src.db.queries import selectAllShelters, insertShelter, selectShelterById
from src.db.errors import ReturnedZeroRowsException
from src.db.models import DBShelterWithoutId

async def getAllShelters():
  db_shelters = await selectAllShelters()
  return [Shelter(
    id=db_shelter.shelter_id,
    name=db_shelter.name,
    address=db_shelter.address,
  ) for db_shelter in db_shelters]

async def getOneShelterById(shelter_id: int):
  try:
    db_shelter = await selectShelterById(shelter_id)
  except ReturnedZeroRowsException:
    raise HTTPException(status_code=404, detail="Shelter not found")

  return Shelter(
    id=db_shelter.shelter_id,
    name=db_shelter.name,
    address=db_shelter.address,
  )

async def createShelter(shelter: ShelterWithoutId) -> Shelter:
  new_shelter_id = await insertShelter(DBShelterWithoutId(
    name=shelter.name,
    address=shelter.address,
  ))
  return Shelter(**shelter.model_dump(), id=new_shelter_id)

async def updateOneShelterById(shelter_id: int, shelter: ShelterWithoutId):
  pass

async def deleteShelterById(shelter_id: int):
  pass
