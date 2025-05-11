from typing import Any

from fastapi import HTTPException, status


class DetailedHTTPException(HTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = "Server error"

    def __init__(self, **kwargs: dict[str, Any]) -> None:
        super().__init__(status_code=self.STATUS_CODE, detail=self.DETAIL, **kwargs)


class BadRequest(DetailedHTTPException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "Bad request"


class ValidationError(BadRequest):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "Passwords do not match."


class InvalidPasswordPatternError(BadRequest):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = """Password must contain: 
            At least eight characters
            Only Latin letters
            At least 1 uppercase letter
            At least 1 special character: $ % & ! : """
