import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.database import database, setup_db
from app.config.logging_conf import configure_logging
from app.users.router import users_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def db_lifespan(application: FastAPI):
    configure_logging()
    await setup_db()
    yield
    await database.close_db()


app = FastAPI(title="SwipeMatch API", lifespan=db_lifespan, root_path="/api")
