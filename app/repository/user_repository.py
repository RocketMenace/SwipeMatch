from typing import Any, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import SessionDep
from app.models.user_models import User
from app.repository.base_repository import BaseRepository


class UserRepository(BaseRepository):

    def __init__(self, session: Annotated[AsyncSession, Depends(SessionDep)]):
        self.session = session
        super().__init__(session=session, model=User)


