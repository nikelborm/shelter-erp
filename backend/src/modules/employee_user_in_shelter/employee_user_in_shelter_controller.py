from icecream import ic
from fastapi import APIRouter
from .models import EmployeeUserInShelter, EmployeeUserInShelterToCreate
from .employee_user_in_shelter_use_case import getAllEmployeeUserInShelters, createEmployeeUserInShelter, deleteEmployeeUserInShelterById, getOneEmployeeUserInShelterById, updateOneEmployeeUserInShelterById

router = APIRouter()

@router.get("/")
async def handleGettingAllEmployeeUserInShelters():
  return await getAllEmployeeUserInShelters()

@router.get("/employeeUserId={employeeUserId}_shelterId={shelterId}/")
async def handleGettingOneEmployeeUserInShelterByIds(employeeUserId: int, shelterId: int):
  return await getOneEmployeeUserInShelterById(employeeUserId, shelterId)

@router.patch("/employeeUserId={employeeUserId}_shelterId={shelterId}/")
async def handleUpdatingOneEmployeeUserInShelterByIds(employeeUserId: int, shelterId: int, employee_user_in_shelter: EmployeeUserInShelter):
  return await updateOneEmployeeUserInShelterById(employeeUserId, shelterId, employee_user_in_shelter)

@router.post("/")
async def handleCreatingEmployeeUserInShelter(employee_user_in_shelter: EmployeeUserInShelterToCreate):
  return await createEmployeeUserInShelter(employee_user_in_shelter)

@router.delete("/employeeUserId={employeeUserId}_shelterId={shelterId}/")
async def handleDeletingEmployeeUserInShelters(employeeUserId: int, shelterId: int):
  return await deleteEmployeeUserInShelterById(employeeUserId, shelterId)
