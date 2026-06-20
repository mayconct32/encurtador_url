from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class InputURL(BaseModel):
    long_url: str


class ReplyURL(BaseModel):
    short_url: str


@app.post("/shorten-url/", response_model=ReplyURL)
def shorten_url(long_url: InputURL):
    pass


@app.get("/{path}")
def access_short_url(path: str):
    pass