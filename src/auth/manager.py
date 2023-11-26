import uuid

from fastapi import Depends
from fastapi_users import BaseUserManager, IntegerIDMixin

from src.auth.db_connect import get_user_db
from src.auth.models import User
from src.config import SECRET


# SECRET = "SECRET"


class UserManager(IntegerIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
