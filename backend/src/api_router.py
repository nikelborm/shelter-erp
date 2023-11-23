from fastapi import APIRouter

from .modules.shelter             import shelter_controller
from .modules.user                import user_controller
from .modules.employee            import employee_controller
from .modules.abstract_pet        import abstract_pet_controller
from .modules.pet_instance        import pet_instance_controller
from .modules.pet_takeout_request import pet_takeout_request_controller


api_router = APIRouter(prefix='/api')

api_router.include_router(shelter_controller.router,             prefix='/shelter')
api_router.include_router(user_controller.router,                prefix='/user')
api_router.include_router(employee_controller.router,            prefix='/employee')
api_router.include_router(abstract_pet_controller.router,        prefix='/abstract_pet')
api_router.include_router(pet_instance_controller.router,        prefix='/pet_instance')
api_router.include_router(pet_takeout_request_controller.router, prefix='/pet_takeout_request')
