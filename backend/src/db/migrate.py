import os
from .tools import DatabaseTransactionManager

async def exec_sql_file(sql_file_name: str):
  with open(os.path.join(os.path.dirname(__file__), sql_file_name)) as migration_file:
    async with DatabaseTransactionManager() as connection:
      return await connection.execute(migration_file.read())

async def migrate():
  await exec_sql_file("migrate.sql")

async def mock():
  await exec_sql_file("mock.sql")
