from src.db.models.user import DBUserWithoutId
from src.tools import DatabaseTransactionManager
from src.config import USER_TABLE_NAME



async def insertUser(user: DBUserWithoutId) -> int:
  async with DatabaseTransactionManager() as connection:
    new_user_id = await connection.fetchval(
      f"insert into {USER_TABLE_NAME}(first_name, second_name, email, phone) values ($1, $2, $3, $4) returning user_id ",
      user.first_name, user.second_name, user.email, user.phone
    )

    if not isinstance(new_user_id,int):
      raise Exception("Failed to create user")

    return new_user_id
