import logging

from fastapi import FastAPI

from app.api.endpoints import user

# logger = logging.getLogger(__name__)


app = FastAPI(title="SwipeMatch API", root_path="/api")

app.include_router(user.router)
