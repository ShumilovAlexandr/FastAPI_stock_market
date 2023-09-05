from fastapi_users.authentication import (BearerTransport,
                                          JWTStrategy,
                                          AuthenticationBackend)

from database.db_config import JWT_SECRET


bearer_transport = BearerTransport(tokenUrl="jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=JWT_SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy
)


