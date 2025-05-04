from typing import Annotated, Any, TypeVar

from fastapi.params import Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import database

DBModel = TypeVar("DBModel", bound=database.Base)


class BaseRepository:
    def __init__(
        self, session: Annotated[AsyncSession, Depends(database.get_session)], model: DBModel
    ):
        self.session = session
        self.model = model

    async def add_one(self, data: dict[str, Any]) -> dict[str, Any]:
        async with self.session as session:
            async with session.begin():
                stmt = insert(self.model).values(data).returning(self.model)
                result = await session.execute(stmt)
                return result.scalar()
