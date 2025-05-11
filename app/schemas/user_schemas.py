from datetime import date
from enum import Enum

from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator

from app.config.exceptions import ValidationError
from app.validators.user import BirthdateValidator, PasswordPatternValidator


class Interests(str, Enum):
    HIKING = "Hiking"
    PHOTOGRAPHY = "Photography"
    COOKING = "Cooking"
    READING = "Reading"
    GAMING = "Gaming"
    TRAVEL = "Travel"
    YOGA = "Yoga"
    MUSIC = "Music"
    PAINTING = "Painting"
    CYCLING = "Cycling"
    DANCING = "Dancing"
    CHESS = "Chess"
    ASTRONOMY = "Astronomy"
    FISHING = "Fishing"
    PROGRAMMING = "Programming"


class InterestBase(BaseModel):
    name: Interests
    user_id: int


class InterestIn(InterestBase):
    pass


class Interest(InterestBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class PreferenceBase(BaseModel):
    user_id: int
    sex: str
    age_from: int
    age_to: int


class PreferenceIn(PreferenceBase):
    pass


class Preference(PreferenceBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class UserBase(BaseModel):
    first_name: str = Field(description="User's first name")
    last_name: str = Field(
        description="User's last name.",
    )
    birthdate: BirthdateValidator
    email: EmailStr
    city: str
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "first_name": "Ryan",
                    "last_name": "Gosling",
                    "birthdate": "1995-08-13",
                    "email": "gosling@gmail.com",
                    "city": "Moscow",
                    "password": "secret password",
                    "repeat_password": "secret password",
                }
            ]
        }
    )


class UserIn(UserBase):
    password: PasswordPatternValidator
    repeat_password: str

    @model_validator(mode="after")
    def check_password_match(self):
        if self.password != self.repeat_password:
            raise ValidationError


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
