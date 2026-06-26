from pydantic import BaseModel, field_validator
import validators
from exceptions import InvalidURLError


class RequestURL(BaseModel):
    """
    Schema for URL shortening requests.

    Validates that the provided URL is well-formed before processing.
    """
    long_url: str

    @field_validator("long_url", mode="after")
    @classmethod
    def validates_long_url(cls, long_url: str):
        """
        Validates that the provided URL is well-formed.

        Args:
            long_url (str): the URL to validate.

        Returns:
            str: the validated URL.

        Raises:
            InvalidURLError: if the URL is not valid.
        """
        if not validators.url(long_url):
            raise InvalidURLError()
        return long_url
        

class ResponseURL(BaseModel):
    """
    Schema for URL shortening responses.
    """
    short_url: str
