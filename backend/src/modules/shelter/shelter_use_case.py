from fastapi import HTTPException
from .models import Shelter, ShelterWithoutId
from .helpers import getDBShelterWithoutId, getShelter
from src.db import selectAllShelters, insertShelter, selectShelterByPk, SHELTER_CNS, ReturnedZeroRowsException


async def getAllShelters():
  db_shelters = await selectAllShelters()
  return [getShelter(db_shelter) for db_shelter in db_shelters]

async def getOneShelterById(shelter_id: int):
  try:
    db_shelter = await selectShelterByPk({ SHELTER_CNS.SHELTER_ID: shelter_id })
  except ReturnedZeroRowsException:
    raise HTTPException(status_code=404, detail="Shelter not found")

  return getShelter(db_shelter)

async def createShelter(shelter: ShelterWithoutId) -> Shelter:
  new_shelter_id = await insertShelter(getDBShelterWithoutId(shelter))
  return Shelter(**shelter.model_dump(), id=new_shelter_id)

async def updateOneShelterById(shelter_id: int, shelter: ShelterWithoutId):
  pass

async def deleteShelterById(shelter_id: int):
  pass
