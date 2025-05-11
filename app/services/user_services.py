from typing import Annotated, Any

from fastapi import Depends

from app.repository.user_repository import UserRepository
from app.schemas.user_schemas import UserIn


class UserService:
    def __init__(self, repository: Annotated[UserRepository, Depends()]):
        self.repository = repository

    async def add_user(self, data: UserIn) -> dict[str, Any]:
        print(data, "&&&&&&&&&&&")
        user_data = data.model_dump()
        return await self.repository.add_one(data=user_data)
