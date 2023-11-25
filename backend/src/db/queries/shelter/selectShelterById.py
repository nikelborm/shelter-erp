from src.tools import DatabaseTransactionManager
from src.db.errors import ReturnedZeroRowsException
from src.db.models import DBShelter
from src.tools import DatabaseTransactionManager
from src.config import SHELTER_TN

async def selectShelterById(shelter_id: int):
  async with DatabaseTransactionManager() as connection:
    shelter = await connection.fetchrow(f'SELECT * from {SHELTER_TN} where shelter_id = $1', shelter_id)

    if shelter is None:
      raise ReturnedZeroRowsException()

    return DBShelter(**shelter)
