from asyncpg.transaction import Transaction
from asyncpg.connection import Connection
from asyncpg import connect
from src.config import DATABASE_HOST, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_PORT, DATABASE_USERNAME

class DatabaseTransactionManager():
  connection: Connection
  transaction: Transaction
  async def __aenter__(self) -> Connection:
    self.connection = await connect(
      user=DATABASE_USERNAME,
      password=DATABASE_PASSWORD,
      database=DATABASE_NAME,
      host=DATABASE_HOST,
      port=DATABASE_PORT,
    )
    self.transaction = await self.connection.transaction()
    await self.transaction.start()
    return self.connection

  async def __aexit__(self, exc_type, exc_value, exc_traceback):
    if exc_type:
      print('exc_type:')
      print(exc_type)
      print('exc_value:')
      print(exc_value)
      print('exc_traceback:')
      print(exc_traceback)
      await self.transaction.rollback()
    else:
      await self.transaction.commit()

    await self.connection.close()
