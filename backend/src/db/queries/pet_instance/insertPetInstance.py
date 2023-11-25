from src.db.errors import ZeroRowsUpdatedException
from src.db.models import DBPetInstanceWithoutIdToInsert
from src.tools import DatabaseTransactionManager
from src.config import SHELTER_TN

async def insertPetInstance(pet_instance: DBPetInstanceWithoutIdToInsert) -> tuple[int, str]:
  async with DatabaseTransactionManager() as connection:
    pet_instance_row = await connection.fetchrow(
      f"insert into {SHELTER_TN}(abstract_pet_id, shelter_id) values ($1, $2) returning pet_instance_id, was_brought_at",
      pet_instance.abstract_pet_id, pet_instance.shelter_id
    )

    if pet_instance_row is None or not isinstance(pet_instance_row.pet_instance_id, int) or not isinstance(pet_instance_row.was_brought_at, str):
      raise ZeroRowsUpdatedException()

    return (pet_instance_row.pet_instance_id, pet_instance_row.was_brought_at)
