from http import HTTPStatus
import os
from cassandra.cluster import ResultSet
from dotenv import load_dotenv
from interfaces import IURLRepository
from exceptions import URLError


load_dotenv()

class URLService:
    def __init__(self, url_repository: IURLRepository) -> None:
        self.url_repository = url_repository
    
    def _create_short_code(self) -> str:
        return "testtest"

    def create_short_url(self, long_url: str) -> str:
        short_code = self._create_short_code()
        self.url_repository.create_short_url(long_url, short_code)
        short_url=os.getenv("BASE_URL") + short_code
        return short_url

    def get_long_url(self, short_code: str) -> str:
        response: ResultSet = self.url_repository.get_long_url(short_code)
        row = response.one()
        if not row:
            raise URLError(
                message="URL not found",
                status_code=HTTPStatus.NOT_FOUND
            )
        return row.long_url    

