import re
from datetime import date, datetime, timedelta
from typing import Annotated

from pydantic import AfterValidator, ValidationError


def birthdate_validator(value: date) -> date:
    if datetime.now().year - value.year < 18:
        raise ValidationError("User must be at least 18 years old")
    return value


def password_pattern_validator(value: str) -> str:
    password_pattern = re.compile(r"^(?=.*\d)(?=.*[!@#$%^&*])[\w!@#$%^&*]{6,128}$")
    if not re.match(password_pattern, value):
        raise ValidationError(
            "Password must contain: "
            "At least eight characters"
            "Only Latin letters"
            "At least 1 uppercase letter"
            "At least 1 special character: $ % & ! : '"
        )
    return value


BirthdateValidator = Annotated[date, AfterValidator(birthdate_validator)]
