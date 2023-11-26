from dataclasses import dataclass, field
from enum import StrEnum
from typing import Generic, TypeVar
from pydantic import BaseModel


def set_of_columns(columns: frozenset[str]) -> frozenset[str]:
  return frozenset({str(k) for k in columns})

def getDollarSequence(length: int) -> str:
  return ', '.join(f'${k + 1}' for k in range(length))

SelectStarModel = TypeVar('SelectStarModel', bound=BaseModel)
PkOnlyModel = TypeVar('PkOnlyModel', bound=BaseModel)
ColumnNamesEnum = TypeVar('ColumnNamesEnum', bound=StrEnum)

@dataclass()
class DbTable(Generic[SelectStarModel, PkOnlyModel, ColumnNamesEnum]):
  table_name: str
  columns: type[ColumnNamesEnum]
  pydanticModelForSelectStar: type[SelectStarModel]
  pydanticPkModel: type[PkOnlyModel]

  always_generated_columns     : frozenset[str] = field(default_factory=frozenset)
  columns_with_defaults        : frozenset[str] = field(default_factory=frozenset)
  readonly_columns             : frozenset[str] = field(default_factory=frozenset)

  pk_columns_list              : list[str]      = field(init=False)
  sql_pk_selector              : str            = field(init=False)
  set_of_all_columns           : frozenset[str] = field(init=False)
  columns_possible_to_insert   : frozenset[str] = field(init=False)
  columns_required_to_insert   : frozenset[str] = field(init=False)
  columns_optional_to_insert   : frozenset[str] = field(init=False)
  columns_possible_to_update   : frozenset[str] = field(init=False)

  def __post_init__(self):
    self.set_of_all_columns = frozenset({str(k) for k in self.columns})

    self.always_generated_columns   = set_of_columns(self.always_generated_columns)
    self.columns_with_defaults      = set_of_columns(self.columns_with_defaults)
    self.readonly_columns           = set_of_columns(self.readonly_columns)
    self.pk_columns_list = list(self.pydanticPkModel.model_fields.keys())

    self.columns_possible_to_insert = self.set_of_all_columns.difference(self.always_generated_columns)
    self.columns_required_to_insert = self.columns_possible_to_insert.difference(self.columns_with_defaults)
    self.columns_optional_to_insert = self.columns_with_defaults
    self.columns_possible_to_update = self.columns_possible_to_insert.difference(self.readonly_columns)

    self.sql_pk_selector = " AND ".join(f"{pk_column_name} = ${index + 1}" for index, pk_column_name in enumerate(self.pk_columns_list))

  def assertCanInsertColumns(self, columns: frozenset[str]):
    if not (self.columns_possible_to_insert.issuperset(columns) and columns.issuperset(self.columns_required_to_insert)):
      raise Exception(f'Cannot insert entity with given set of columns: {columns}')

  def assertCanUpdateColumns(self, columns: frozenset[str]):
    if not self.columns_possible_to_update.issuperset(columns):
      raise Exception(f'Cannot update entity with given set of columns: {columns}')

  def has_pk_columns(self, columns: frozenset[str]) -> bool:
    return frozenset(self.pk_columns_list).issubset(columns)

  def consist_only_of_pk_columns(self, columns: frozenset[str]) -> bool:
    return frozenset(self.pk_columns_list) == columns

  def get_generated_columns(self, columns: frozenset[str]) -> frozenset[str]:
    return self.always_generated_columns.union(self.columns_with_defaults.difference(columns))

  def plain_select_all_query(self):
    return f'SELECT * FROM {self.table_name}'

  def plain_select_by_pk_query(self):
    return f'SELECT * FROM {self.table_name} WHERE {self.sql_pk_selector}'

  def plain_insert_query(self, givenColumnsList: list[str]):
    query = f"""INSERT INTO {self.table_name}({', '.join(givenColumnsList)})
                VALUES ({getDollarSequence(len(givenColumnsList))})"""
    generated_columns = self.get_generated_columns(frozenset(givenColumnsList))
    if len(generated_columns):
      query += f" RETURNING {', '.join(generated_columns)}"
    return query

  def plain_update_query(self, columnsToSetValueList: list[str]):
    return  f"""UPDATE {self.table_name}
                SET {', '.join(
                  f'{pk_column_name} = ${index + 1 + len(self.pk_columns_list)}'
                  for index, pk_column_name in enumerate(columnsToSetValueList)
                )}
                WHERE {self.sql_pk_selector}"""

  def plain_delete_query(self):
    return  f'''DELETE FROM {self.table_name}
                WHERE {self.sql_pk_selector}
                RETURNING {", ".join(self.pk_columns_list)}'''
