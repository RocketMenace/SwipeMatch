from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import database
from app.repository.interest import InterestRepository
from app.repository.preference import PreferenceRepository
from app.repository.user_repository import UserRepository


def get_user_repository(
    session: Annotated[AsyncSession, Depends(database.get_session)],
):
    return UserRepository(session=session)


def get_preference_repository(
    session: Annotated[AsyncSession, Depends(database.get_session)],
):
    return PreferenceRepository(session=session)


