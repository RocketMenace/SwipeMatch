from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user_models import Interest
from app.repository.base_repository import BaseRepository


class PreferenceRepository(BaseRepository):
    def __init__(self, session: Annotated[AsyncSession, Depends()]):
        self.session = session
        super().__init__(session=session, model=Interest)
