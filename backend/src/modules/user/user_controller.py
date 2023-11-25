from fastapi import APIRouter
from .user_use_case import UserWithoutId, getAllUsers, createUser, deleteUserById, getOneUserById, updateOneUserById

router = APIRouter()

@router.get("/")
async def handleGettingAllUsers():
  return await getAllUsers()

@router.get("/{user_id}/")
async def handleGettingOneUserById(user_id: int):
  return await getOneUserById(user_id)

@router.patch("/{user_id}/")
async def handleUpdatingOneUserById(user_id: int, user: UserWithoutId):
  return await updateOneUserById(user_id, user)

@router.post("/")
async def handleCreatingUser(user: UserWithoutId):
  return await createUser(user)

@router.delete("/{user_id}/")
async def handleDeletingUser(user_id: int):
  return await deleteUserById(user_id)
