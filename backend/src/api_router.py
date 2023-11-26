from fastapi import APIRouter
from .modules import shelter_router, user_router, employee_user_router, employee_user_in_shelter_router, abstract_pet_router, pet_instance_router, pet_takeout_request_router


api_router = APIRouter(prefix='/api')

api_router.include_router(shelter_router,                  prefix='/shelters')
api_router.include_router(user_router,                     prefix='/users')
api_router.include_router(employee_user_router,            prefix='/employeeUsers')
api_router.include_router(employee_user_in_shelter_router, prefix='/employeeUserInShelters')
api_router.include_router(abstract_pet_router,             prefix='/abstractPets')
api_router.include_router(pet_instance_router,             prefix='/petInstances')
api_router.include_router(pet_takeout_request_router,      prefix='/petTakeoutRequests')
