from fastapi import HTTPException
from icecream import ic
from src.db import selectAllUsers, insertUser, selectUserByPk, ZeroRowsReturnedException, DBUserPk, deleteUserByPk, updateUserByPk, ZeroRowsAffectedException, USER_CNS
from .models import User, UserWithoutId
from .helpers import getDBUserWithoutId, getUser


async def getAllUsers():
  db_users = await selectAllUsers()
  return [getUser(db_user) for db_user in db_users]

async def getOneUserById(user_id: int):
  try:
    db_user = await selectUserByPk(DBUserPk(user_id=user_id))
  except ZeroRowsReturnedException:
    raise HTTPException(status_code=404, detail="User you tried to get was not found")

  return getUser(db_user)

async def createUser(user: UserWithoutId) -> User:
  user_record = await insertUser(getDBUserWithoutId(user))
  return User(**user.model_dump(), id=user_record[USER_CNS.USER_ID])

async def updateOneUserById(user_id: int, user: UserWithoutId):
  try:
    await updateUserByPk(user, DBUserPk(user_id=user_id))
  except ZeroRowsAffectedException:
    raise HTTPException(status_code=404, detail="User you tried to update was not found")

async def deleteUserById(user_id: int):
  try:
    await deleteUserByPk(DBUserPk(user_id=user_id))
  except ZeroRowsAffectedException:
    raise HTTPException(status_code=404, detail="User you tried to update was not found")
