from src.tools import DatabaseTransactionManager
from src.db.errors import ReturnedZeroRowsException
from src.db.models import DBPetInstance
from src.tools import DatabaseTransactionManager
from src.config import PET_INSTANCE_TN

async def selectPetInstanceById(pet_instance_id: int):
  async with DatabaseTransactionManager() as connection:
    pet_instance = await connection.fetchrow(f'SELECT * from {PET_INSTANCE_TN} where pet_instance_id = $1', pet_instance_id)

    if pet_instance is None:
      raise ReturnedZeroRowsException()

    return DBPetInstance(**pet_instance)
