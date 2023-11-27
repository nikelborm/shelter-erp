from ..models import PetTakeoutRequest, PetTakeoutRequestWithoutId, PetTakeoutRequestToCreate
from src.db import DBPetTakeoutRequestWithoutId, DBPetTakeoutRequest, DBPetTakeoutRequestToInsert

def getDBPetTakeoutRequestWithoutId(pet_takeout_request: PetTakeoutRequestWithoutId) -> DBPetTakeoutRequestWithoutId:
  return DBPetTakeoutRequestWithoutId(
    adopter_user_id=pet_takeout_request.adopterUserId,
    shelter_id=pet_takeout_request.shelterId,
    employee_user_id=pet_takeout_request.employeeUserId,
    pet_instance_id=pet_takeout_request.petInstanceId,
    status=pet_takeout_request.status,
    created_at=pet_takeout_request.createdAt,
    resolved_at=pet_takeout_request.resolvedAt,
  )

def getDBPetTakeoutRequestToInsert(pet_takeout_request: PetTakeoutRequestToCreate) -> DBPetTakeoutRequestToInsert:
  return DBPetTakeoutRequestToInsert(
    adopter_user_id=pet_takeout_request.adopterUserId,
    shelter_id=pet_takeout_request.shelterId,
    employee_user_id=pet_takeout_request.employeeUserId,
    pet_instance_id=pet_takeout_request.petInstanceId,
    status=pet_takeout_request.status,
    created_at=pet_takeout_request.createdAt,
    resolved_at=pet_takeout_request.resolvedAt,
  )

def getPetTakeoutRequestWithoutId(db_pet_takeout_request: DBPetTakeoutRequestWithoutId) -> PetTakeoutRequestWithoutId:
  return PetTakeoutRequestWithoutId(
    adopterUserId=db_pet_takeout_request.adopter_user_id,
    shelterId=db_pet_takeout_request.shelter_id,
    employeeUserId=db_pet_takeout_request.employee_user_id,
    petInstanceId=db_pet_takeout_request.pet_instance_id,
    status=db_pet_takeout_request.status,
    createdAt=db_pet_takeout_request.created_at,
    resolvedAt=db_pet_takeout_request.resolved_at,
  )

def getDBPetTakeoutRequest(pet_takeout_request: PetTakeoutRequest) -> DBPetTakeoutRequest:
  return DBPetTakeoutRequest(
    pet_takeout_request_id=pet_takeout_request.id,
    **getDBPetTakeoutRequestWithoutId(pet_takeout_request).model_dump(),
  )

def getPetTakeoutRequest(db_pet_takeout_request: DBPetTakeoutRequest) -> PetTakeoutRequest:
  return PetTakeoutRequest(
    id=db_pet_takeout_request.pet_takeout_request_id,
    **getPetTakeoutRequestWithoutId(db_pet_takeout_request).model_dump(),
  )
