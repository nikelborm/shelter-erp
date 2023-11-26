from pydantic import BaseModel, EmailStr

class DBUserWithoutId(BaseModel):
  first_name: str
  second_name: str
  email: EmailStr
  phone: str

class DBUserPk(BaseModel):
  user_id: int

class DBUser(DBUserWithoutId, DBUserPk):
  pass
