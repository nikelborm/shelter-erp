from pydantic import BaseModel

class AbstractPetWithoutId(BaseModel):
  parentAbstractPetId: int | None
  petClassName: str

class AbstractPet(AbstractPetWithoutId):
  id: int
