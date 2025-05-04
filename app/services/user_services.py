from app.repository.user_repository import UserRepository
from app.schemas.user_schemas import UserIn


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, data: UserIn):
        user_data = data.model_dump()
        user = await self.user_repository.create(data=user_data)
        return user
