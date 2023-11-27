from fastapi import HTTPException
from .models import PetTakeoutRequest, PetTakeoutRequestWithoutId, PetTakeoutRequestToCreate
from .helpers import getPetTakeoutRequest, getDBPetTakeoutRequestToInsert
from src.db import selectAllPetTakeoutRequests, insertPetTakeoutRequest, selectPetTakeoutRequestByPk, ZeroRowsReturnedException, DBPetTakeoutRequestPk, deletePetTakeoutRequestByPk, updatePetTakeoutRequestByPk, ZeroRowsAffectedException, PET_TAKEOUT_REQUEST_CNS, PetTakeoutRequestStatusEnum


async def getAllPetTakeoutRequests():
  db_pet_takeout_requests = await selectAllPetTakeoutRequests()
  return [getPetTakeoutRequest(db_pet_takeout_request) for db_pet_takeout_request in db_pet_takeout_requests]

async def getOnePetTakeoutRequestById(pet_takeout_request_id: int):
  try:
    db_pet_takeout_request = await selectPetTakeoutRequestByPk(DBPetTakeoutRequestPk(pet_takeout_request_id=pet_takeout_request_id))
  except ZeroRowsReturnedException:
    raise HTTPException(status_code=404, detail="PetTakeoutRequest you tried to get was not found")

  return getPetTakeoutRequest(db_pet_takeout_request)

async def createPetTakeoutRequest(pet_takeout_request: PetTakeoutRequestToCreate) -> PetTakeoutRequest:
  columnsWithDefaults = { PET_TAKEOUT_REQUEST_CNS.CREATED_AT }
  model_to_insert = getDBPetTakeoutRequestToInsert(pet_takeout_request)
  if pet_takeout_request.status is None:
    delattr(model_to_insert, PET_TAKEOUT_REQUEST_CNS.STATUS)
    columnsWithDefaults.add(PET_TAKEOUT_REQUEST_CNS.STATUS)
    setattr(model_to_insert, PET_TAKEOUT_REQUEST_CNS.RESOLVED_AT, None)
  else:
    if pet_takeout_request.status == PetTakeoutRequestStatusEnum.UNDECIDED:
      setattr(model_to_insert, PET_TAKEOUT_REQUEST_CNS.RESOLVED_AT, None)
    else:
      columnsWithDefaults.add(PET_TAKEOUT_REQUEST_CNS.RESOLVED_AT)


  pet_takeout_request_record = await insertPetTakeoutRequest(model_to_insert, frozenset(columnsWithDefaults))
  return PetTakeoutRequest(
    **pet_takeout_request.model_dump(),
    id=pet_takeout_request_record[PET_TAKEOUT_REQUEST_CNS.PET_TAKEOUT_REQUEST_ID],
    status=pet_takeout_request_record.get(PET_TAKEOUT_REQUEST_CNS.RESOLVED_AT, pet_takeout_request.status),
    createdAt=pet_takeout_request_record[PET_TAKEOUT_REQUEST_CNS.CREATED_AT],
    resolvedAt=pet_takeout_request_record.get(PET_TAKEOUT_REQUEST_CNS.RESOLVED_AT, None)
  )

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
