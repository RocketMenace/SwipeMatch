from typing import Annotated, Any

from fastapi import Depends

from app.repository.interest import InterestRepository
from app.schemas.user_schemas import InterestIn


class InterestService:
    def __init__(self, repository: Annotated[InterestRepository, Depends()]):
        self.repository = repository

    async def add_interest(self, data: InterestIn) -> dict[str, Any]:
        interest_data = data.model_dump()
        return await self.repository.add_one(interest_data)
