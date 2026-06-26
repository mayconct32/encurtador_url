from pydantic import BaseModel, field_validator
import validators
from exceptions import InvalidURLError


class RequestURL(BaseModel):
    long_url: str

    @field_validator("long_url", mode="after")
    @classmethod
    def validates_long_url(cls, long_url: str):
        if not validators.url(long_url):
            raise InvalidURLError()
        return long_url
        

class ResponseURL(BaseModel):
    short_url: str
