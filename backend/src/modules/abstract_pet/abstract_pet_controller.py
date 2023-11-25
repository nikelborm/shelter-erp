from fastapi import APIRouter
from .abstract_pet_use_case import AbstractPetWithoutId, getAllAbstractPets, createAbstractPet, deleteAbstractPetById, getOneAbstractPetById, updateOneAbstractPetById

router = APIRouter()

@router.get("/")
async def handleGettingAllAbstractPets():
  return await getAllAbstractPets()

@router.get("/{abstract_pet_id}/")
async def handleGettingOneAbstractPetById(abstract_pet_id: int):
  return await getOneAbstractPetById(abstract_pet_id)

@router.patch("/{abstract_pet_id}/")
async def handleUpdatingOneAbstractPetById(abstract_pet_id: int, abstract_pet: AbstractPetWithoutId):
  return await updateOneAbstractPetById(abstract_pet_id, abstract_pet)

@router.post("/")
async def handleCreatingAbstractPet(abstract_pet: AbstractPetWithoutId):
  return await createAbstractPet(abstract_pet)

@router.delete("/{abstract_pet_id}/")
async def handleDeletingAbstractPet(abstract_pet_id: int):
  return await deleteAbstractPetById(abstract_pet_id)
