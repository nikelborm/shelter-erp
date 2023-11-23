from src.tools import DatabaseTransactionManager
from src.db.models.user import DBUser
from src.tools import DatabaseTransactionManager
from src.config import USER_TABLE_NAME

async def selectAllUsers():
  async with DatabaseTransactionManager() as connection:
    users = await connection.fetch(f'SELECT * from {USER_TABLE_NAME}')
    return [DBUser(**user) for user in users]
