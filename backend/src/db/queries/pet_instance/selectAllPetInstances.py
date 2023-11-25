from src.tools import DatabaseTransactionManager
from src.db.models import DBPetInstance
from src.tools import DatabaseTransactionManager
from src.config import PET_INSTANCE_TN

async def selectAllPetInstances():
  async with DatabaseTransactionManager() as connection:
    petInstances = await connection.fetch(f'SELECT * from {PET_INSTANCE_TN}')
    return [DBPetInstance(**petInstance) for petInstance in petInstances]
