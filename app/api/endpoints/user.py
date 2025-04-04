from typing import Any, Annotated

from fastapi import APIRouter, status, Depends
from app.schemas.user_schemas import UserIn, User
from app.services.user_services import UserService
from app.dependencies.user import user_service


router = APIRouter(prefix="/users", tags=["Users"])


@router.post(path="/register", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(data: UserIn, service: Annotated[UserService, Depends(user_service)]):
    return await service.create_user(data)
