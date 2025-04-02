from datetime import date

from pydantic import BaseModel, EmailStr

class Interest(BaseModel):
    pass

class Preference(BaseModel):
    pass

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
    pass

