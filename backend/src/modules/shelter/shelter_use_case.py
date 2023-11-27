from fastapi import HTTPException
from .models import Shelter, ShelterWithoutId
from .helpers import getDBShelterWithoutId, getShelter
from src.db import selectAllShelters, insertShelter, selectShelterByPk, ZeroRowsReturnedException, DBShelterPk, deleteShelterByPk, updateShelterByPk, ZeroRowsAffectedException, SHELTER_CNS


async def getAllShelters():
  db_shelters = await selectAllShelters()
  return [getShelter(db_shelter) for db_shelter in db_shelters]

async def getOneShelterById(shelter_id: int):
  try:
    db_shelter = await selectShelterByPk(DBShelterPk(shelter_id=shelter_id))
  except ZeroRowsReturnedException:
    raise HTTPException(status_code=404, detail="Shelter you tried to get was not found")

  return getShelter(db_shelter)

async def createShelter(shelter: ShelterWithoutId) -> Shelter:
  shelter_record = await insertShelter(getDBShelterWithoutId(shelter))
  return Shelter(**shelter.model_dump(), id=shelter_record[SHELTER_CNS.SHELTER_ID])

async def updateOneShelterById(shelter_id: int, shelter: ShelterWithoutId):
  try:
    await updateShelterByPk(shelter, DBShelterPk(shelter_id=shelter_id))
  except ZeroRowsAffectedException:
    raise HTTPException(status_code=404, detail="Shelter you tried to update was not found")

async def deleteShelterById(shelter_id: int):
  try:
    await deleteShelterByPk(DBShelterPk(shelter_id=shelter_id))
  except ZeroRowsAffectedException:
    raise HTTPException(status_code=404, detail="Shelter you tried to update was not found")
