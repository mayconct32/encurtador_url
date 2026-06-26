from abc import ABC, abstractmethod
from typing import Any


class IURLRepository(ABC):
    """
    Interface for URL repository operations.

    All repository implementations must inherit from this class
    and implement its abstract methods.
    """
    @abstractmethod
    def get_short_url(self, short_code: str) -> Any:
        """
        Checks if a short code exists in the database.

        Args:
            short_code (str): the short code to check.

        Returns:
            Any: query result containing the short code if found.

        Raises:
            URLNotFoundError: if the short code is not found.
        """
        pass

    @abstractmethod
    def create_short_url(self, long_url: str, short_code: str) -> Any:
        """
        Creates a new short URL mapping in the database.

        Args:
            long_url (str): the original long URL.
            short_code (str): the generated short code.

        Returns:
            Any: query result of the insert operation.
        """
        pass

    @abstractmethod
    def get_long_url(self, short_code: str) -> Any:
        """
        Retrieves the long URL associated with a short code.

        Args:
            short_code (str): the short code to look up.

        Returns:
            Any: query result containing the long URL.

        Raises:
            URLNotFoundError: if no URL is found for the given short code.
        """
        pass


class IDBConnection(ABC):
    """
    Interface for database connection operations.

    All database connection implementations must inherit from this class
    and implement its abstract methods.
    """
    @property
    @abstractmethod
    def session(self) -> Any:
        """
        Returns the active database session.

        Returns:
            Any: the database session object.
        """
        pass
    
    @abstractmethod
    def execute(self, query: str, params: Any = None) -> Any:
        """
        Executes a database query with optional parameters.

        Args:
            query (str): the SQL/CQL query to execute.
            params (Any): optional query parameters.

        Returns:
            Any: query result.
        """
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """
        Shuts down the database connection.

        Returns:
            None
        """
        pass
