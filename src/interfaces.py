from abc import ABC, abstractmethod
from typing import Any


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
