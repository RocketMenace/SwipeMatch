import re
from datetime import date, datetime
from typing import Annotated

from pydantic import AfterValidator, ValidationError
from app.config.exceptions import InvalidPasswordPatternError


def birthdate_validator(value: date) -> date:
    if datetime.now().year - value.year < 18:
        raise ValidationError("User must be at least 18 years old")
    return value


def password_pattern_validator(value: str) -> str:
    password_pattern = re.compile(r"^(?=.*\d)(?=.*[!@#$%^&*])[\w!@#$%^&*]{6,128}$")
    if not re.match(password_pattern, value):
        raise InvalidPasswordPatternError()
    return value


PasswordPatternValidator = Annotated[str, AfterValidator(password_pattern_validator)]
BirthdateValidator = Annotated[date, AfterValidator(birthdate_validator)]
