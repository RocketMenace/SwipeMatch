from typing import Annotated, Any

from fastapi import Depends

from app.repository.preference import PreferenceRepository
from app.schemas.user_schemas import PreferenceIn


class PreferenceService:
    def __init__(self, repository: Annotated[PreferenceRepository, Depends()]):
        self.repository = repository

    async def add_preference(self, data: PreferenceIn):
        preference_data = data.model_dump()
        return await self.repository.add_one(preference_data)
