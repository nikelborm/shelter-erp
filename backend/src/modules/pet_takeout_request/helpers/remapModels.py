from ..models import PetTakeoutRequest, PetTakeoutRequestWithoutId
from src.db import DBPetTakeoutRequestWithoutId, DBPetTakeoutRequest

def getDBPetTakeoutRequestWithoutId(shelter: PetTakeoutRequestWithoutId) -> DBPetTakeoutRequestWithoutId:
  return DBPetTakeoutRequestWithoutId(
    adopter_user_id=shelter.adopterUserId,
    shelter_id=shelter.shelterId,
    employee_user_id=shelter.employeeUserId,
    pet_instance_id=shelter.petInstanceId,
    status=shelter.status,
    created_at=shelter.createdAt,
    resolved_at=shelter.resolvedAt,
  )

def getPetTakeoutRequestWithoutId(db_shelter: DBPetTakeoutRequestWithoutId) -> PetTakeoutRequestWithoutId:
  return PetTakeoutRequestWithoutId(
    adopterUserId=db_shelter.adopter_user_id,
    shelterId=db_shelter.shelter_id,
    employeeUserId=db_shelter.employee_user_id,
    petInstanceId=db_shelter.pet_instance_id,
    status=db_shelter.status,
    createdAt=db_shelter.created_at,
    resolvedAt=db_shelter.resolved_at,
  )

def getDBPetTakeoutRequest(shelter: PetTakeoutRequest) -> DBPetTakeoutRequest:
  return DBPetTakeoutRequest(
    shelter_id=shelter.id,
    **getDBPetTakeoutRequestWithoutId(shelter).model_dump(),
  )

def getPetTakeoutRequest(db_shelter: DBPetTakeoutRequest) -> PetTakeoutRequest:
  return PetTakeoutRequest(
    id=db_shelter.shelter_id,
    **getPetTakeoutRequestWithoutId(db_shelter).model_dump(),
  )
