from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.schemas.user_schemas import User, UserIn
from app.services.user_services import UserService

router = APIRouter(prefix="", tags=["Users"])


@router.post(
    path="/register",
    status_code=status.HTTP_201_CREATED,
    response_model=User,
    summary="Create user profile.",
)
async def create_user(data: UserIn, service: Annotated[UserService, Depends()]):
    return await service.add_user(data=data)
