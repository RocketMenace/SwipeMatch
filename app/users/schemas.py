from datetime import date

from pydantic import BaseModel, EmailStr


class InterestBase(BaseModel):
    name: str


class InterestIn(InterestBase):
    pass


class Interest(InterestBase):
    id: int


class PreferenceBase(BaseModel):
    user_id: int
    sex: str
    age_from: int
    age_to: int


class PreferenceIn(PreferenceBase):
    pass


class Preference(PreferenceBase):
    id: int


class UserBase(BaseModel):
    first_name: str
    last_name: str
    birthdate: date  #  Need validation for user's ages over 18
    email: EmailStr
    city: str
    interests: list[Interest]
    preferences: Preference


class UserIn(UserBase):
    password: str
    repeat_password: str


class User(UserBase):
    id: int
