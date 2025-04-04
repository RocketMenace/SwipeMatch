from typing import AnyStr, Any

from app.repository.base_repository import BaseRepository
from app.core.dependencies import SessionDep
from app.schemas.user_schemas import UserIn
from app.models.user_models import User


class UserRepository(BaseRepository):
    def __init__(self, session: SessionDep):
        self.session = session

    async def create(
        self,
        data: dict[str, Any],
    ) -> dict[str, Any]:
        async with self.session.begin() as session:
            return await session.add(User(**data))
