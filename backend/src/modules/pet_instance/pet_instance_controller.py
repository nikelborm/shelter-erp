from fastapi import APIRouter
from .pet_instance_use_case import PetInstanceWithoutId, getAllPetInstances, createPetInstance, deletePetInstanceById, getOnePetInstanceById, updateOnePetInstanceById

router = APIRouter()

@router.get("/")
async def handleGettingAllPetInstances():
  return await getAllPetInstances()

@router.get("/{pet_instance_id}/")
async def handleGettingOnePetInstanceById(pet_instance_id: int):
  return await getOnePetInstanceById(pet_instance_id)

@router.patch("/{pet_instance_id}/")
async def handleUpdatingOnePetInstanceById(pet_instance_id: int, pet_instance: PetInstanceWithoutId):
  return await updateOnePetInstanceById(pet_instance_id, pet_instance)

@router.post("/")
async def handleCreatingPetInstance(pet_instance: PetInstanceWithoutId):
  return await createPetInstance(pet_instance)

@router.delete("/{pet_instance_id}/")
async def handleDeletingPetInstance(pet_instance_id: int):
  return await deletePetInstanceById(pet_instance_id)
