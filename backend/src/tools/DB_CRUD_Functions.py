from enum import StrEnum
from typing import Generic, TypeVar
from pydantic import BaseModel
from src.db.errors import ReturnedZeroRowsException, ZeroRowsUpdatedException
from .DatabaseTransactionManager import DatabaseTransactionManager
from .DbTable import DbTable

def getDollarSequence(length: int) -> str:
  return ', '.join(f'${k + 1}' for k in range(length))

SelectStarModel = TypeVar('SelectStarModel', bound=BaseModel)
ColumnNamesEnum = TypeVar('ColumnNamesEnum', bound=StrEnum)

class DB_CRUD_Functions(Generic[SelectStarModel, ColumnNamesEnum]):
  PascalSingularName: str
  PascalPluralName: str
  dbTable: DbTable[SelectStarModel, ColumnNamesEnum]
  def __init__(self, PascalSingularName: str, PascalPluralName: str, dbTable: DbTable[SelectStarModel, ColumnNamesEnum]):
    self.PascalSingularName = PascalSingularName
    self.PascalPluralName = PascalPluralName
    self.dbTable = dbTable

  async def selectAllEntities(self):
    async with DatabaseTransactionManager() as connection:
      entities = await connection.fetch(f'SELECT * from {self.dbTable.table_name}')
      return [self.dbTable.pydanticModelForSelectStar(**entity) for entity in entities]

  async def selectEntityByPk(self, **entity_pk_columns):
    givenPkColumnsList = list(entity_pk_columns.keys())

    if not self.dbTable.consist_only_of_pk_columns(frozenset(givenPkColumnsList)):
      raise Exception(f'Cannot select entity with given set of pk columns: {entity_pk_columns.keys()}')

    async with DatabaseTransactionManager() as connection:
      entity = await connection.fetchrow(
        f'SELECT * from {self.dbTable.table_name} where {" AND ".join(f"{pk_column_name} = ${index + 1}" for index, pk_column_name in enumerate(givenPkColumnsList))}',
        *(entity_pk_columns[k] for k in givenPkColumnsList)
      )
      if entity is None:
        raise ReturnedZeroRowsException()
      return self.dbTable.pydanticModelForSelectStar(**entity)

  async def insertEntity(self, dbEntity: BaseModel) -> int:
    givenColumnsList = list(dbEntity.__class__.model_fields.keys())
    givenColumnsSet = frozenset(givenColumnsList)

    # Db entity should not have always generated columns
    if not self.dbTable.canInsertColumns(givenColumnsSet):
      raise Exception(f'Cannot insert entity with given set of columns: {givenColumnsSet}')

    async with DatabaseTransactionManager() as connection:
      generated_components = await connection.fetchrow(
        f"""insert into {self.dbTable.table_name}({', '.join(givenColumnsList)})
        values ({getDollarSequence(len(givenColumnsList))})
        returning {', '.join(self.dbTable.get_generated_columns(givenColumnsSet))} """,
        *(getattr(dbEntity, column_name) for column_name in givenColumnsList)
      )

      if not generated_components:
        raise ZeroRowsUpdatedException()

      return generated_components

  async def updateEntityByPk(self, dbEntityWithoutPk: BaseModel, **entity_pk_columns):
    pass

  async def deleteEntityByPk(self, **entity_pk_columns):
    pass
