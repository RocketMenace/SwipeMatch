from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.schemas.user_schemas import Interest, InterestIn
from app.services.interest import InterestService

router = APIRouter(prefix="/interest", tags=["Interests"])


@router.post(path="/add", status_code=status.HTTP_201_CREATED, response_model=Interest)
async def add_interest(
    data: InterestIn, service: Annotated[InterestService, Depends()]
):
    return await service.add_interest(data)
