from typing import Annotated

from fastapi import Depends

from app.dependencies.repository import (get_interest_repository,
                                         get_preference_repository,
                                         get_user_repository)
from app.repository.interest import InterestRepository
from app.repository.preference import PreferenceRepository
from app.repository.user_repository import UserRepository
from app.services.interest import InterestService
from app.services.preference import PreferenceService
from app.services.user_services import UserService


def get_user_service(
    repository: Annotated[UserRepository, Depends(get_user_repository)],
):
    return UserService(repository=repository)


def get_interest_service(
    repository: Annotated[InterestRepository, Depends(get_interest_repository)],
):
    return InterestService(repository=repository)


def get_preference_service(
    repository: Annotated[PreferenceRepository, Depends(get_preference_repository)],
):
    return PreferenceService(repository=repository)
