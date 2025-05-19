from app.repository.user_repository import UserRepository
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import database

def get_user_repository(session: Annotated[AsyncSession, Depends(database.get_session)]):
    return UserRepository(session)