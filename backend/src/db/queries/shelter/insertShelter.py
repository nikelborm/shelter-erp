from src.db.errors import ZeroRowsUpdatedException
from src.db.models import DBShelterWithoutId
from src.tools import DatabaseTransactionManager
from src.config import SHELTER_TN

async def insertShelter(shelter: DBShelterWithoutId) -> int:
  async with DatabaseTransactionManager() as connection:
    new_shelter_id = await connection.fetchval(
      f"insert into {SHELTER_TN}(address, name) values ($1, $2) returning shelter_id ",
      shelter.address, shelter.name
    )

    if not isinstance(new_shelter_id, int):
      raise ZeroRowsUpdatedException()

    return new_shelter_id
