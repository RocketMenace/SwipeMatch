from fastapi import APIRouter, status


users_router = APIRouter()


@users_router.post(path="/users", status_code=status.HTTP_201_CREATED)
async def create(data):
    pass
