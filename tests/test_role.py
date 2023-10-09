import pytest

from sqlalchemy import (insert,
                        select)
from conftest import client

from conftest import async_session_maker
from src.auth.models import Role


# async def test_add_role():
#     """Тест при ручном добавлении без использования маршрута."""
#     async with async_session_maker() as session:
#         stmt = insert(Role).values(id=1, name="admin")
#
#         await session.execute(stmt)
#         await session.commit()
#
#         query = select(Role.id, Role.name).where(Role.name == "admin")
#         result = await session.execute(query)
#         assert result.all() == [(1, "admin")], "Ошибка при добавлении роли."
#
# async def test_add_role_api():
#     """Добавление роли через API."""
#     response = client.post("/role", json={
#         "id": 2,
#         "name": "Trader"
#     })
#     assert response.status_code == 201
#
# async def test_get_role():
#     """Тест на получение данных об одной роли из бд."""
#     response = client.get("/role/{id}",
#                           params={"role_id": 2
#                                   })
#     assert response.status_code == 200
#
# async def test_get_list_role():
#     """Тест на получение данных о ролях из бд."""
#     response = client.get("/role")
#     assert response.status_code == 200
