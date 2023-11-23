from fastapi import APIRouter
from .user_use_case import UserWithoutId, getAllUsers, createUser, deleteUser, createMockUsers

router = APIRouter()

@router.get("/")
async def handleGettingAllUsers():
  return await getAllUsers()

@router.post("/")
async def handleCreatingUser(user: UserWithoutId):
  return await createUser(user)

@router.delete("/")
async def handleDeletingUser():
  return await deleteUser()

@router.post("/createMockRecords")
async def handleCreatingMockUsers():
  return await createMockUsers()
