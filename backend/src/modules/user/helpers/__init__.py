from src.modules.user.models import User, UserWithoutId
from src.db.models import DBUserWithoutId, DBUser

def getDBUserWithoutId(user: UserWithoutId) -> DBUserWithoutId:
  return DBUserWithoutId(
    first_name=user.firstName,
    second_name=user.secondName,
    email=user.email,
    phone=user.phone,
  )

def getUserWithoutId(db_user: DBUserWithoutId) -> UserWithoutId:
  return UserWithoutId(
    firstName=db_user.first_name,
    secondName=db_user.second_name,
    email=db_user.email,
    phone=db_user.phone,
  )

def getDBUser(user: User) -> DBUser:
  return DBUser(
    user_id=user.id,
    **getDBUserWithoutId(user).model_dump(),
  )

def getUser(db_user: DBUser) -> User:
  return User(
    id=db_user.user_id,
    **getUserWithoutId(db_user).model_dump(),
  )
