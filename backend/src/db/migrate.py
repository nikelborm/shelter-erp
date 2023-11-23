from src.tools import DatabaseTransactionManager

async def migrate():
  with open("migrate.sql") as migration_file:
    async with DatabaseTransactionManager() as connection:
      return await connection.execute(migration_file.read())
