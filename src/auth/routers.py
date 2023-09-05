from fastapi import (APIRouter,
                     Depends)
from fastapi_users import FastAPIUsers

from .schemas import (CreateUser,
                      Role)
from database.db_conn import (AsyncSession,
                              get_session)


router_role = APIRouter(
    prefix="/role",
    tags=["role"]
)


@router_role.post("/users")
async def create_role(role: Role,
                      session: AsyncSession = Depends(get_session)):
    """Создание роли (сохранение её в БД)."""
    ...


