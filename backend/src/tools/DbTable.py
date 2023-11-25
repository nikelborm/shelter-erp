from dataclasses import dataclass, field
from enum import StrEnum

from pydantic import BaseModel


def set_of_columns(columns: frozenset[str]) -> frozenset[str]:
  return frozenset({str(k) for k in columns})

@dataclass()
class DbTable():
  table_name: str
  columns: type[StrEnum]
  pydanticModelForSelectStar: type[BaseModel]
  always_generated_columns     : frozenset[str] = field(default_factory=frozenset)
  columns_with_defaults        : frozenset[str] = field(default_factory=frozenset)
  pk_columns                   : frozenset[str] = field(default_factory=frozenset)
  readonly_columns             : frozenset[str] = field(default_factory=frozenset)
  set_of_all_columns           : frozenset[str] = field(init=False)
  columns_possible_to_insert   : frozenset[str] = field(init=False)
  columns_required_to_insert   : frozenset[str] = field(init=False)
  columns_optional_to_insert   : frozenset[str] = field(init=False)
  columns_possible_to_update   : frozenset[str] = field(init=False)
  def __post_init__(self):
    self.set_of_all_columns = frozenset({str(k) for k in self.columns})
    self.always_generated_columns   = set_of_columns(self.always_generated_columns)
    self.columns_with_defaults      = set_of_columns(self.columns_with_defaults)
    self.pk_columns                 = set_of_columns(self.pk_columns)
    self.readonly_columns           = set_of_columns(self.readonly_columns)
    self.columns_possible_to_insert = self.set_of_all_columns.difference(self.always_generated_columns)
    self.columns_required_to_insert = self.columns_possible_to_insert.difference(self.columns_with_defaults)
    self.columns_optional_to_insert = self.columns_with_defaults
    self.columns_possible_to_update = self.columns_possible_to_insert.difference(self.readonly_columns)
  def canInsertColumns(self, columns: frozenset[str]) -> bool:
    return self.columns_possible_to_insert.issuperset(columns) and columns.issuperset(self.columns_required_to_insert)
  def canUpdateColumns(self, columns: frozenset[str]) -> bool:
    return self.columns_possible_to_update.issuperset(columns)
  def has_pk_columns(self, columns: frozenset[str]) -> bool:
    return self.pk_columns.issubset(columns)
  def get_generated_columns(self, columns: frozenset[str]) -> frozenset[str]:
    return self.always_generated_columns.union(self.columns_with_defaults.difference(columns))
