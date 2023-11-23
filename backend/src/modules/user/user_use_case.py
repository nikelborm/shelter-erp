from src.tools import DatabaseTransactionManager
from src.config import USER_TABLE_NAME

async def getAllUsers():
  async with DatabaseTransactionManager() as connection:
    return await connection.execute(f'SELECT * from {USER_TABLE_NAME};')

async def createUser():
  pass

async def deleteUser():
  pass

async def createMockUsers():
  pass
