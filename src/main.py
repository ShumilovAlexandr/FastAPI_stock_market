from fastapi import FastAPI
from fastapi_users import (FastAPIUsers,
                           fastapi_users)

from auth.models import User
from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.schemas import (ReadUser,
                          CreateUser)
from auth.routers import router_role


app = FastAPI(
    title="Stock data",
    description="Приложения для просмотра данных фондовой биржи",
)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=True),
    prefix="/auth/jwt",
    tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(ReadUser, CreateUser),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_role)
current_user = fastapi_users.current_user()


# TODO пишу тесты!!!


