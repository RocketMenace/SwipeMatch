import logging

from fastapi import FastAPI

from app.api.endpoints import user

# logger = logging.getLogger(__name__)


app = FastAPI(title="Users Service API", root_path="/users")

app.include_router(user.router)
