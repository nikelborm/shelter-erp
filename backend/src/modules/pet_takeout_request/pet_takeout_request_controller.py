from fastapi import APIRouter
from .models import PetTakeoutRequestWithoutId
from .pet_takeout_request_use_case import getAllPetTakeoutRequests, createPetTakeoutRequest, deletePetTakeoutRequestById, getOnePetTakeoutRequestById, updateOnePetTakeoutRequestById, PetTakeoutRequestToCreate

router = APIRouter()

@router.get("/")
async def handleGettingAllPetTakeoutRequests():
  return await getAllPetTakeoutRequests()

@router.get("/{pet_takeout_request_id}/")
async def handleGettingOnePetTakeoutRequestById(pet_takeout_request_id: int):
  return await getOnePetTakeoutRequestById(pet_takeout_request_id)

@router.patch("/{pet_takeout_request_id}/")
async def handleUpdatingOnePetTakeoutRequestById(pet_takeout_request_id: int, pet_takeout_request: PetTakeoutRequestWithoutId):
  return await updateOnePetTakeoutRequestById(pet_takeout_request_id, pet_takeout_request)

@router.post("/")
async def handleCreatingPetTakeoutRequest(pet_takeout_request: PetTakeoutRequestToCreate):
  return await createPetTakeoutRequest(pet_takeout_request)

@router.delete("/{pet_takeout_request_id}/")
async def handleDeletingPetTakeoutRequest(pet_takeout_request_id: int):
  return await deletePetTakeoutRequestById(pet_takeout_request_id)
