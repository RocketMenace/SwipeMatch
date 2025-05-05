from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.validators.user import BirthdateValidator


class InterestBase(BaseModel):
    name: str
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
    birthdate: BirthdateValidator  #  Need validation for user's ages over 18
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
                    "password": "secretpassword",
                    "repeat_password": "secretpassword",
                }
            ]
        }
    )


class UserIn(UserBase):
    password: str
    repeat_password: str


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
