from typing import Annotated

from app.services.user_services import UserService
from app.repository.user_repository import UserRepository
from fastapi import Depends
from app.dependencies.repository import get_user_repository

def get_user_service(repository: Annotated[UserRepository, Depends(get_user_repository)]):
    return UserService(repository=repository)