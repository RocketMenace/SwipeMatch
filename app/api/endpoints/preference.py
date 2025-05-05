from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.schemas.user_schemas import Preference, PreferenceIn
from app.services.preference import PreferenceService

router = APIRouter(prefix="/preferences", tags=["Preferences"])


@router.post("/add", status_code=status.HTTP_201_CREATED, response_model=Preference)
async def add_preference(
    data: PreferenceIn, service: Annotated[PreferenceService, Depends()]
):
    return await service.add_preference(data=data)
