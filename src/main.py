from fastapi import FastAPI, APIRouter
from fastapi_users import FastAPIUsers
from src.auth.models import User
from src.auth.manager import get_user_manager
from src.auth.auth import auth_backend
from src.auth.schemas import UserRead, UserCreate
from src.back_list.scripts import category_router, record_router
from src.imports.scripts import import_router
from src.adapter_kafka.scripts import kafka_router

app = FastAPI(
    title="My BackList"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/back-list/auth/jwt",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/back-list/auth",
    tags=["Auth"],
)

app.include_router(category_router)

app.include_router(record_router)

app.include_router(kafka_router)

app.include_router(import_router)
