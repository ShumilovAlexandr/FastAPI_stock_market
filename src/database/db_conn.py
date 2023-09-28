from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import (create_async_engine,
                                    AsyncSession)
from sqlalchemy.orm import sessionmaker
from fastapi_users.db import SQLAlchemyUserDatabase

from .db_config import (DB_USER,
                        DB_PASS,
                        DB_HOST,
                        DB_PORT,
                        DB_NAME)
from auth.models import (Base,
                         User)


DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:' \
               f'{DB_PORT}/{DB_NAME}'


engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession,
                             expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_session)):
    yield SQLAlchemyUserDatabase(session, User)

