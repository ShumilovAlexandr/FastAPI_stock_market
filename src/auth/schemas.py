from pydantic import (BaseModel,
                      field_validator,
                      EmailStr)
from email_validator import (validate_email,
                             EmailNotValidError)
from fastapi_users import schemas


class CreateUser(schemas.BaseUserCreate):
    email: str | None
    role_id: int
    username: str
    hashed_password: str
    is_active: bool | None = True
    is_superuser: bool | None = False
    is_verified: bool | None = False

    @field_validator('email')
    @classmethod
    def verify_email(cls, email: EmailStr) -> str:
        try:
            email_info = validate_email(email,
                                        check_deliverability=False)
            email = email_info.normalized
        except EmailNotValidError:
            raise ValueError("Электронная почта задана в не верном формате!")
        return email


class ReadUser(schemas.BaseUser[int]):
    id: int
    email: str | None
    role_id: int
    username: str
    is_active: bool | None = True
    is_superuser: bool | None = False
    is_verified: bool | None = False

    class Config:
        orm_mode = True


class Role(BaseModel):
    id: int
    name: str | None

