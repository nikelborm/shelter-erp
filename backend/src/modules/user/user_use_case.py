from src.db.queries import selectAllUsers, insertUser
from src.db.models import DBUserWithoutId
from pydantic import BaseModel, EmailStr

class UserWithoutId(BaseModel):
  firstName: str
  secondName: str
  email: EmailStr
  phone: str

class User(UserWithoutId):
  id: int

async def getAllUsers():
  db_users = await selectAllUsers()
  return [User(
    id=user.user_id,
    firstName=user.first_name,
    secondName=user.second_name,
    email=user.email,
    phone=user.phone
  ) for user in db_users]

async def createUser(user: UserWithoutId) -> User:
  new_user_id = await insertUser(DBUserWithoutId(
    first_name=user.firstName,
    second_name=user.secondName,
    email=user.email,
    phone=user.phone
  ))
  return User(**user.model_dump(), id=new_user_id)

async def deleteUser():
  pass
