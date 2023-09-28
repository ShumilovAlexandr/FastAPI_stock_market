import sqlalchemy.exc
from fastapi import (APIRouter,
                     Depends,
                     status,
                     HTTPException)
from sqlalchemy import select

from .schemas import (CreateUser,
                      RoleCreateGet)
from .models import Role
from database.db_conn import get_session
from sqlalchemy.ext.asyncio import AsyncSession


router_role = APIRouter(
    prefix="/role",
    tags=["role"]
)


@router_role.post("/", status_code=status.HTTP_201_CREATED)
async def create_role(role: RoleCreateGet,
                      session: AsyncSession = Depends(get_session)):
    """Создание роли (сохранение её в БД)."""
    try:
        db_role = Role(**role.dict())
        session.add(db_role)
        await session.commit()
        return {"data": db_role}
    except Exception:
        raise HTTPException(status_code=422, detail="Некорректный вод данных")


@router_role.get("/{id}")
async def get_role(role_id: int,
                   session: AsyncSession = Depends(get_session)):
    """Роутер возвращает одну интересующую роль."""
    try:
        stmt = select(Role).where(Role.id == role_id)
        result_role = await session.execute(stmt)
        return result_role.scalar()
    except sqlalchemy.exc.OperationalError:
        return "Ошибка при извлечении информации о роли"

@router_role.get("/")
async def get_list_roles(session: AsyncSession = Depends(get_session)):
    """Роутер возвращает список имеющихся ролей."""
    try:
        stmt = select(Role)
        result_role = await session.execute(stmt)
        return result_role.scalars().all()
    except sqlalchemy.exc.OperationalError:
        return "Ошибка при извлечении информации о роли"


