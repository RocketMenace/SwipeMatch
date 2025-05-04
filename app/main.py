import logging

from fastapi import FastAPI

from app.api.endpoints.user import router

logger = logging.getLogger(__name__)


app = FastAPI(title="SwipeMatch API", root_path="/api")

app.include_router(router)
