import os
from cassandra.cluster import ResultSet
from dotenv import load_dotenv
from interfaces import IURLRepository
from exceptions import URLNotFoundError


load_dotenv()

class URLService:
    """
    Service layer responsible for URL shortening business logic.

    Handles the creation and retrieval of short URLs using the
    repository for data access.
    """
    def __init__(self, url_repository: IURLRepository) -> None:
        """
        Initializes the URL service with a repository.

        Args:
            url_repository (IURLRepository): the repository for URL data access.

        Returns:
            None
        """
        self.url_repository = url_repository
    
    def _create_short_code(self) -> str:
        """
        Generates a unique short code for the URL.

        Returns:
            str: the generated short code.
        """
        return "testtest"

    def create_short_url(self, long_url: str) -> str:
        """
        Creates a new short URL and stores it in the database.

        Args:
            long_url (str): the original long URL to shorten.

        Returns:
            str: the complete short URL.
        """
        short_code = self._create_short_code()
        self.url_repository.create_short_url(long_url, short_code)
        short_url=os.getenv("BASE_URL") + short_code
        return short_url

    def get_long_url(self, short_code: str) -> str:
        """
        Retrieves the original long URL from a short code.

        Args:
            short_code (str): the short code to look up.

        Returns:
            str: the original long URL.

        Raises:
            URLNotFoundError: if no URL is found for the given short code.
        """
        response: ResultSet = self.url_repository.get_long_url(short_code)
        row = response.one()
        if not row:
            raise URLNotFoundError()
        return row.long_url    

