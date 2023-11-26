from fastapi import APIRouter
from .models import ShelterWithoutId
from .shelter_use_case import getAllShelters, createShelter, deleteShelterById, getOneShelterById, updateOneShelterById

router = APIRouter()

@router.get("/")
async def handleGettingAllShelters():
  return await getAllShelters()

@router.get("/{shelter_id}/")
async def handleGettingOneShelterById(shelter_id: int):
  return await getOneShelterById(shelter_id)

@router.patch("/{shelter_id}/")
async def handleUpdatingOneShelterById(shelter_id: int, shelter: ShelterWithoutId):
  return await updateOneShelterById(shelter_id, shelter)

@router.post("/")
async def handleCreatingShelter(shelter: ShelterWithoutId):
  return await createShelter(shelter)

@router.delete("/{shelter_id}/")
async def handleDeletingShelter(shelter_id: int):
  return await deleteShelterById(shelter_id)
