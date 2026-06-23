from abc import ABC, abstractmethod
from typing import Any, Optional


class IURLRepository(ABC):
    @abstractmethod
    def get_short_url(self, short_code: str) -> str:
        pass

    @abstractmethod
    def create_short_url(self, long_url: str, url_path: str) -> Optional[str]:
        pass

    @abstractmethod
    def get_long_url(self, url_path: str) -> str:
        pass


class IDBConnection(ABC):
    @property
    @abstractmethod
    def session(self) -> Any:
        pass
    
    @abstractmethod
    def execute(self, query: str, params: Any = None) -> Any:
        pass

    @abstractmethod
    def shutdown(self) -> None:
        pass
