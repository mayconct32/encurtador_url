from pydantic import BaseModel


class RequestURL(BaseModel):
    long_url: str


class ResponseURL(BaseModel):
    short_url: str
