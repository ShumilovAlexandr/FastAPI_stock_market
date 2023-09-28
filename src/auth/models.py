from datetime import datetime
from sqlalchemy.orm import (DeclarativeBase,
                            Mapped,
                            mapped_column)
from sqlalchemy import (String,
                        ForeignKey,
                        TIMESTAMP)
from fastapi_users.db import SQLAlchemyBaseUserTable


class Base(DeclarativeBase):
    pass


class Role(Base):
    __tablename__ = "role"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(30))
    role_id: Mapped[str] = mapped_column(ForeignKey("role.id"))
    registered_at: Mapped[str] = mapped_column(TIMESTAMP,
                                               default=datetime.utcnow)
    username: Mapped[str] = mapped_column(String(30))
    hashed_password: Mapped[str] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)

