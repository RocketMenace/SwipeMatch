import json

from sqlalchemy import insert

from app.config.database import database
from app.models.user_models import Interest


async def import_from_json():
    async with open("interests_fixture.json", "r") as buffer:
        data = json.loads(buffer)

    async with database.get_session() as session:
        async with session.begin():
            stmt = insert(Interest).values(data)
            await session.execute(stmt)

if __name__ == "__main__":
    import_from_json()
