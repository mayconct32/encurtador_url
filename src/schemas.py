from http import HTTPStatus
from pydantic import BaseModel, field_validator
import validators
from exceptions import URLError


class RequestURL(BaseModel):
    long_url: str

    @field_validator("long_url", mode="after")
    @classmethod
    def validates_long_url(cls, long_url: str):
        if not validators.url(long_url):
            raise URLError(
                message = "Invalid URL",
                status_code = HTTPStatus.UNPROCESSABLE_CONTENT
            )
        return long_url
        

class ResponseURL(BaseModel):
    short_url: str
