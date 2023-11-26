from enum import StrEnum
from typing import Generic, TypeVar
from pydantic import BaseModel

from ..errors import ZeroRowsReturnedException, ZeroRowsAffectedException
from .DatabaseTransactionManager import DatabaseTransactionManager
from .DbTable import DbTable


SelectStarModel = TypeVar('SelectStarModel', bound=BaseModel)
PkOnlyModel = TypeVar('PkOnlyModel', bound=BaseModel)
ColumnNamesEnum = TypeVar('ColumnNamesEnum', bound=StrEnum)


class DB_CRUD_Functions(Generic[SelectStarModel, PkOnlyModel, ColumnNamesEnum]):
  PascalSingularName: str
  PascalPluralName: str
  dbTable: DbTable[SelectStarModel, PkOnlyModel, ColumnNamesEnum]
  def __init__(self, PascalSingularName: str, PascalPluralName: str, dbTable: DbTable[SelectStarModel, PkOnlyModel, ColumnNamesEnum]):
    self.PascalSingularName = PascalSingularName
    self.PascalPluralName = PascalPluralName
    self.dbTable = dbTable

  async def selectAllEntities(self):
    async with DatabaseTransactionManager() as connection:
      entities = await connection.fetch(self.dbTable.plain_select_all_query())
      print(entities)
      return [self.dbTable.pydanticModelForSelectStar(**entity) for entity in entities]

  async def selectEntityByPk(self, entity_pk: PkOnlyModel):
    self.assert_is_pk(entity_pk)

    async with DatabaseTransactionManager() as connection:
      entity = await connection.fetchrow(
        self.dbTable.plain_select_by_pk_query(),
        *(getattr(entity_pk, pk_column_name) for pk_column_name in self.dbTable.pk_columns_list)
      )

      if entity is None:
        raise ZeroRowsReturnedException()

      return self.dbTable.pydanticModelForSelectStar(**entity)

  async def insertEntity(self, dbEntity: BaseModel) -> int:
    givenColumnsList = list(dbEntity.model_fields.keys())

    # Db entity should not have always generated columns
    self.dbTable.assertCanInsertColumns(frozenset(givenColumnsList))

    async with DatabaseTransactionManager() as connection:
      generated_components = await connection.fetchrow(
        self.dbTable.plain_insert_query(givenColumnsList),
        *(getattr(dbEntity, column_name) for column_name in givenColumnsList)
      )

      if not generated_components:
        raise ZeroRowsAffectedException()

      return generated_components

  async def updateEntityByPk(self, dbEntityWithoutPk: BaseModel, entity_pk: PkOnlyModel):
    self.assert_is_pk(entity_pk)
    givenColumnsList = list(dbEntityWithoutPk.model_fields.keys())
    self.dbTable.assertCanUpdateColumns(frozenset(givenColumnsList))

    async with DatabaseTransactionManager() as connection:
      entity = await connection.fetchrow(
        self.dbTable.plain_update_query(givenColumnsList),
        *(getattr(entity_pk, pk_column_name) for pk_column_name in self.dbTable.pk_columns_list)
      )

      if entity is None:
        raise ZeroRowsAffectedException()

  async def deleteEntityByPk(self, entity_pk: PkOnlyModel):
    self.assert_is_pk(entity_pk)

    async with DatabaseTransactionManager() as connection:
      entity = await connection.fetchrow(
        self.dbTable.plain_delete_query(),
        *(getattr(entity_pk, pk_column_name) for pk_column_name in self.dbTable.pk_columns_list)
      )

      if entity is None:
        raise ZeroRowsAffectedException()

  def assert_is_pk(self, entity_pk: PkOnlyModel):
    if not isinstance(entity_pk, self.dbTable.pydanticPkModel):
      raise Exception(f'entity_pk({entity_pk}) is not instance of {self.dbTable.pydanticPkModel.__name__}')
