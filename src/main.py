from random import choice
import string
from fastapi import FastAPI, Request
from pydantic import BaseModel


app = FastAPI()

class InputURL(BaseModel):
    long_url: str


class ReplyURL(BaseModel):
    short_url: str


memory_db = {}


# This code is temporary. Collisions will occur in the future.
NUMBERS_OF_CHARACTERS = 4
def random_path():
    random_string = "".join(
        choice(string.ascii_letters + string.digits) 
        for _ in range(NUMBERS_OF_CHARACTERS)
    )
    return random_string


@app.post("/shorten-url/")
def shorten_url(url: InputURL, request: Request):
    path = random_path()
    memory_db[path] = url.long_url
    return ReplyURL(
        short_url = request.base_url._url + path
    )


@app.get("/{path}")
def access_short_url(path: str):
    pass