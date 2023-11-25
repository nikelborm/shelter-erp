from pydantic import BaseModel, EmailStr

class UserWithoutId(BaseModel):
  firstName: str
  secondName: str
  email: EmailStr
  phone: str

class User(UserWithoutId):
  id: int
