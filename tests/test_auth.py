import pytest

from conftest import client


async def test_register():
    response = client.post("/auth/register", json={
        "email": "sanya.sumilov1993@gmail.com",
        "password": "qwerty54321",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "role_id": 1,
        "username": "string"
    })
    assert response.status_code == 201


