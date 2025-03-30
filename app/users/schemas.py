from datetime import date

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: str
    birthdate: date  #  Need validation for user's ages over 18
    email: EmailStr


class UserIn(UserBase):
    password: str
    repeat_password: str


class User(UserBase):
    pass
