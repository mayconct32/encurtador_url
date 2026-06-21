from random import choice
from http import HTTPStatus
import os
import string
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from pydantic_settings import BaseSettings
import validators


load_dotenv()

app = FastAPI()


class InputURL(BaseModel):
    long_url: str


class ReplyURL(BaseModel):
    short_url: str


# This is a temporary database; it will soon be replaced by a real database.
memory_db = {}


# This code is temporary. Collisions will occur in the future.
NUMBERS_OF_CHARACTERS = 4
def random_path():
    random_string = "".join(
        choice(string.ascii_letters + string.digits) 
        for _ in range(NUMBERS_OF_CHARACTERS)
    )
    return random_string


@app.post("/shorten-url/", response_model=ReplyURL)
def shorten_url(url: InputURL, request: Request):
    if not validators.url(url.long_url):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Invalid URL"
        )
    path = random_path()
    memory_db[path] = url.long_url
    return ReplyURL(
        short_url=os.getenv("BASE_URL") + path
    )


@app.get("/{path}")
def access_short_url(path: str):
    if path not in memory_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="URL not found"
        )
    return RedirectResponse(memory_db[path])
