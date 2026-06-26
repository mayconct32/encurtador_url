from typing import Annotated
from http import HTTPStatus
from fastapi import FastAPI, Depends, Request
from fastapi.responses import RedirectResponse, JSONResponse
from schemas import RequestURL, ResponseURL
from dependencies import get_url_service
from service import URLService
from exceptions import URLError


app = FastAPI()

url_service_type = Annotated[URLService, Depends(get_url_service)]


@app.post("/shorten-url/", response_model=ResponseURL)
def shorten_url(url: RequestURL, url_service: url_service_type):
    """
    Creates a shortened URL from the provided long URL.

    Args:
        url (RequestURL): the request body containing the long URL.
        url_service (URLService): the URL service instance.

    Returns:
        ResponseURL: the response containing the shortened URL.

    Raises:
        InvalidURLError: if the provided URL is not valid.
    """
    short_url = url_service.create_short_url(url.long_url)
    return ResponseURL(short_url=short_url)


@app.get("/{short_code}")
def access_short_url(short_code: str, url_service: url_service_type):
    """
    Redirects to the original URL using the provided short code.

    Args:
        short_code (str): the short code to look up.
        url_service (URLService): the URL service instance.

    Returns:
        RedirectResponse: redirect to the original long URL.

    Raises:
        URLNotFoundError: if no URL is found for the given short code.
    """
    long_url = url_service.get_long_url(short_code)
    return RedirectResponse(long_url)


@app.exception_handler(URLError)
def url_exception_handler(request: Request, exc: URLError):
    """
    Handles application-specific URL errors.

    Args:
        request (Request): the incoming HTTP request.
        exc (URLError): the URL error exception.

    Returns:
        JSONResponse: JSON response with error details.
    """
    return JSONResponse(
        status_code = exc.status_code,
        content={"error": exc.message}
    )


@app.exception_handler(Exception)
def url_exception_handler(request: Request, exc: Exception):
    """
    Handles unexpected generic exceptions.

    Args:
        request (Request): the incoming HTTP request.
        exc (Exception): the generic exception.

    Returns:
        JSONResponse: JSON response with internal server error.
    """
    return JSONResponse(
        status_code = HTTPStatus.INTERNAL_SERVER_ERROR,
        content={"error": "Internal server error"}
    )