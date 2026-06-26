from typing import Optional
from http import HTTPStatus


class URLError(Exception):
    """
    Base application exception with a custom status code and message. 

    All other specific exceptions must inherit from this class so that
    the global handler can process them in a standardized way.
    """
    def __init__(self, message: str, status_code: HTTPStatus) -> None:
        """
        Initializes the exception with a status code and message.

        Args:
            message (str): error message.
            status_code (HTTPStatus): error status code.

        Returns:
            None
        """
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class URLNotFoundError(URLError):
    """Exception thrown when the URL is not found."""
    def __init__(self, message: Optional[str] = None) -> None:
        """
        Initializes the exception with a status code and message.

        Args:
            message (str): error message.

        Returns:
            None
        """
        super().__init__(
            message = message or "URL not found",
            status_code = HTTPStatus.NOT_FOUND
        )


class InvalidURLError(URLError):
    """Exception thrown when the URL is invalid."""
    def __init__(self, message: Optional[str] = None) -> None:
        """
        Initializes the exception with a status code and message.

        Args:
            message (str): error message.

        Returns:
            None
        """
        super().__init__(
            message = message or "Invalid URL",
            status_code = HTTPStatus.UNPROCESSABLE_CONTENT
        )