from abc import ABC, abstractmethod
from typing import Any, Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import SessionDep


class BaseRepository(ABC):
    @abstractmethod
    async def create(self, data: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError
