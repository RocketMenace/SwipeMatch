import logging

from fastapi import FastAPI

from app.api.endpoints import interest, preference, user

# logger = logging.getLogger(__name__)


app = FastAPI(title="Users Service API", root_path="/users")

app.include_router(user.router)
app.include_router(interest.router)
app.include_router(preference.router)
