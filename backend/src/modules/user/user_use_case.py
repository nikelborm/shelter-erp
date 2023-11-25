from fastapi import HTTPException
from .models import User, UserWithoutId
from .helpers import getDBUserWithoutId, getUser
from src.db.queries import selectAllUsers, insertUser, selectUserById
from src.db.errors import ReturnedZeroRowsException
from src.db.models import DBUserWithoutId

async def getAllUsers():
  db_users = await selectAllUsers()
  return [getUser(db_user) for db_user in db_users]

async def getOneUserById(user_id: int):
  try:
    db_user = await selectUserById(user_id)
  except ReturnedZeroRowsException:
    raise HTTPException(status_code=404, detail="User not found")

  return getUser(db_user)

async def createUser(user: UserWithoutId) -> User:
  new_user_id = await insertUser(getDBUserWithoutId(user))
  return User(**user.model_dump(), id=new_user_id)

async def updateOneUserById(user_id: int, user: UserWithoutId):
  pass

async def deleteUserById(user_id: int):
  pass
