from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.dependencies.user import user_service
from app.schemas.user_schemas import User, UserIn
from app.services.user_services import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(path="/register", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(
    data: UserIn, service: Annotated[UserService, Depends(user_service)]
):
    return await service.create_user(data)
