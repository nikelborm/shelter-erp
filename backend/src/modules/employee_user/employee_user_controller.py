from fastapi import APIRouter
from .models import EmployeeUserWithoutId, EmployeeUser
from .employee_user_use_case import getAllEmployeeUsers, createEmployeeUser, deleteEmployeeUserById, getOneEmployeeUserById, updateOneEmployeeUserById

router = APIRouter()

@router.get("/")
async def handleGettingAllEmployeeUsers():
  return await getAllEmployeeUsers()

@router.get("/{employee_user_id}/")
async def handleGettingOneEmployeeUserById(employee_user_id: int):
  return await getOneEmployeeUserById(employee_user_id)

@router.patch("/{employee_user_id}/")
async def handleUpdatingOneEmployeeUserById(employee_user_id: int, employee_user: EmployeeUserWithoutId):
  return await updateOneEmployeeUserById(employee_user_id, employee_user)

@router.post("/")
async def handleCreatingEmployeeUser(employee_user: EmployeeUser):
  return await createEmployeeUser(employee_user)

@router.delete("/{employee_user_id}/")
async def handleDeletingEmployeeUser(employee_user_id: int):
  return await deleteEmployeeUserById(employee_user_id)
