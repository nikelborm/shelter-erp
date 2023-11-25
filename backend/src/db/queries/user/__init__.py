from collections import namedtuple
from dataclasses import dataclass
from enum import StrEnum
from typing import Any, List, Type, TypeVar, Literal
from pydantic import BaseModel

from src.config import USER_TN, USER_CNS
from src.db.errors import ReturnedZeroRowsException, ZeroRowsUpdatedException
from src.db.models import DBUserWithoutId, DBUser
from src.tools import DatabaseTransactionManager, DbTable


class DB_CRUD_Functions():
  PascalSingularName: str
  PascalPluralName: str
  dbTable: DbTable
  def __init__(self, PascalSingularName: str, PascalPluralName: str, dbTable: DbTable):
    self.PascalSingularName = PascalSingularName
    self.PascalPluralName = PascalPluralName
    self.dbTable = dbTable

  async def insertEntity(self, dbEntity: BaseModel) -> int:
    givenColumnsList = list(dbEntity.__class__.model_fields.keys())
    givenColumnsSet = frozenset(givenColumnsList)

    # Db entity should not have always generated columns
    if not self.dbTable.canInsertColumns(givenColumnsSet):
      raise Exception(f'Cannot insert entity with given set of columns: {givenColumnsSet}')

    async with DatabaseTransactionManager() as connection:
      new_entity_id = await connection.fetchval(
        f"""insert into {self.dbTable.table_name}({', '.join(givenColumnsList)})
        values ({', '.join(f'${k + 1}' for k in range(len(givenColumnsList)))})
        returning {', '.join(self.dbTable.get_generated_columns(givenColumnsSet))} """,
        *(getattr(dbEntity, column_name) for column_name in givenColumnsList)
      )

      if not isinstance(new_entity_id, int):
        raise ZeroRowsUpdatedException()

      return new_entity_id

  async def selectAllEntities(self):
    async with DatabaseTransactionManager() as connection:
      entities = await connection.fetch(f'SELECT * from {TN}')
      return [DBUser(**entity) for entity in entities]

  async def selectEntityById(self, entity_id: int):
    async with DatabaseTransactionManager() as connection:
      entity = await connection.fetchrow(f'SELECT * from {TN} where entity_id = $1', entity_id)
      if entity is None:
        raise ReturnedZeroRowsException()
      return DBUser(**entity)

  async def updateEntityById(self, entity_id: int, entity: DBUserWithoutId):
    pass

#   Functions = namedtuple(f"{PascalSingularName}Functions", [
#     f"insert{PascalSingularName}",
#     f"selectAll{PascalPluralName}",
#     f"select{PascalSingularName}ById",
#     f"update{PascalSingularName}ById"]
#   )

#   return Functions(
#     insertEntity,
#     selectAllEntities,
#     selectEntityById,
#     updateEntityById,
#   )

# asd = build_DB_CRUD_functions(Literal['User'], Literal['Users'], USER_TN, USER_CNS)
# asd.
