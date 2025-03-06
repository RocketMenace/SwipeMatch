from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.database import setup_db, database


@asynccontextmanager
async def db_lifespan(application: FastAPI):
    await setup_db()
    yield
    await database.close_db()

app = FastAPI(title="SwipeMatch API", lifespan=db_lifespan)