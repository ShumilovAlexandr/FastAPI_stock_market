import pytest

from typing import AsyncGenerator
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import (AsyncSession,
                                    create_async_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from fastapi.testclient import TestClient

from src.main import app
from src.auth.models import Base
from src.database.db_conn import (DB_HOST,
                                  DB_NAME,
                                  DB_PASS,
                                  DB_PORT,
                                  DB_USER)


client = TestClient(app)

DATABASE_URL = f"postgres+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}" \
               f"/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, popclass=NullPool)
async_session_maker = sessionmaker(engine, class_=AsyncSession,
                                   expire_on_commit=False)
Base.metadata(bind=engine)


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

app.dependency_overrides[get_session] = override_get_async_session


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.drop_all)


@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
