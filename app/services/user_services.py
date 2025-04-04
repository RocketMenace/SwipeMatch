from app.repository.base_repository import BaseRepository
from app.schemas.user_schemas import UserIn


class UserService:
    def __init__(self, user_repository: BaseRepository):
        self.user_repository = user_repository

    async def create_user(self, data: UserIn):
        data = data.model_dump()
        user = self.user_repository.create(data)
        return user
