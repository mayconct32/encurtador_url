from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from schemas import RequestURL, ResponseURL
from dependencies import get_url_service
from service import URLService


app = FastAPI()

url_service_type = Annotated[URLService, Depends(get_url_service)]


@app.post("/shorten-url/", response_model=ResponseURL)
def shorten_url(url: RequestURL, url_service: url_service_type):
    short_url = url_service.create_short_url(url.long_url)
    return ResponseURL(short_url=short_url)


@app.get("/{short_code}")
def access_short_url(short_code: str, url_service: url_service_type):
    long_url = url_service.get_long_url(short_code)
    return RedirectResponse(long_url)
