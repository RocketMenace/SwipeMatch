from typing import Any, AnyStr

from app.core.dependencies import SessionDep
from app.models.user_models import User
from app.repository.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, session: SessionDep):
        self.session = session

    async def create(
        self,
        data: dict[str, Any],
    ) -> dict[str, Any]:
        async with self.session.begin() as session:
            return await session.add(User(**data))
