from typing import Annotated

from fastapi import Depends

from app.dependencies.repository import get_user_repository
from app.repository.user_repository import UserRepository
from app.services.user_services import UserService


def get_user_service(
    repository: Annotated[UserRepository, Depends(get_user_repository)],
):
    return UserService(repository=repository)
