from src.tools import DatabaseTransactionManager
from src.db.models import DBShelter
from src.tools import DatabaseTransactionManager
from src.config import SHELTER_TN

async def selectAllShelters():
  async with DatabaseTransactionManager() as connection:
    shelters = await connection.fetch(f'SELECT * from {SHELTER_TN}')
    return [DBShelter(**shelter) for shelter in shelters]
