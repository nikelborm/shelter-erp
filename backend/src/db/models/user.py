from pydantic import BaseModel, EmailStr

class DBUserWithoutId(BaseModel):
  first_name: str
  second_name: str
  email: EmailStr
  phone: str

class DBUser(DBUserWithoutId):
  user_id: int
