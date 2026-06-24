from dotenv import load_dotenv
from interfaces import IURLRepository


load_dotenv()

class URLService:
    def __init__(self, url_repository: IURLRepository) -> None:
        self.url_repository = url_repository
