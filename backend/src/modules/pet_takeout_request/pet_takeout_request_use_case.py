from fastapi import HTTPException
from .models import PetTakeoutRequest, PetTakeoutRequestWithoutId
from .helpers import getDBPetTakeoutRequestWithoutId, getPetTakeoutRequest
from src.db import selectAllPetTakeoutRequests, insertPetTakeoutRequest, selectPetTakeoutRequestByPk, ZeroRowsReturnedException, DBPetTakeoutRequestPk, deletePetTakeoutRequestByPk, updatePetTakeoutRequestByPk, ZeroRowsAffectedException


async def getAllPetTakeoutRequests():
  db_pet_takeout_requests = await selectAllPetTakeoutRequests()
  return [getPetTakeoutRequest(db_pet_takeout_request) for db_pet_takeout_request in db_pet_takeout_requests]

async def getOnePetTakeoutRequestById(pet_takeout_request_id: int):
  try:
    db_pet_takeout_request = await selectPetTakeoutRequestByPk(DBPetTakeoutRequestPk(pet_takeout_request_id=pet_takeout_request_id))
  except ZeroRowsReturnedException:
    raise HTTPException(status_code=404, detail="PetTakeoutRequest you tried to get was not found")

  return getPetTakeoutRequest(db_pet_takeout_request)

async def createPetTakeoutRequest(pet_takeout_request: PetTakeoutRequestWithoutId) -> PetTakeoutRequest:
  new_pet_takeout_request_id = await insertPetTakeoutRequest(getDBPetTakeoutRequestWithoutId(pet_takeout_request))
  return PetTakeoutRequest(**pet_takeout_request.model_dump(), id=new_pet_takeout_request_id)

async def updateOnePetTakeoutRequestById(pet_takeout_request_id: int, pet_takeout_request: PetTakeoutRequestWithoutId):
  try:
    await updatePetTakeoutRequestByPk(pet_takeout_request, DBPetTakeoutRequestPk(pet_takeout_request_id=pet_takeout_request_id))
  except ZeroRowsAffectedException:
    raise HTTPException(status_code=404, detail="PetTakeoutRequest you tried to update was not found")

async def deletePetTakeoutRequestById(pet_takeout_request_id: int):
  try:
    await deletePetTakeoutRequestByPk(DBPetTakeoutRequestPk(pet_takeout_request_id=pet_takeout_request_id))
  except ZeroRowsAffectedException:
    raise HTTPException(status_code=404, detail="PetTakeoutRequest you tried to update was not found")
