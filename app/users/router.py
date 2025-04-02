from fastapi import APIRouter, status
from sqlalchemy.sql.annotation import Annotated

from app.users.schemas import User, UserIn

users_router = APIRouter()


@users_router.post(path="/register", status_code=status.HTTP_201_CREATED)
async def register(data: UserIn, service: Annotated):
    pass
