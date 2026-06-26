from interfaces import IURLRepository, IDBConnection
from typing import Any


class CassandraDBURLRepository(IURLRepository):
    """
    Class responsible for interacting with the 
    database (data access layer).
    """
    def __init__(self, db_connection: IDBConnection) -> None:
        """
        Initializes the repository with a database connection.

        Args:
            db_connection (IDBConnection): the database connection instance.

        Returns:
            None
        """
        self._db_connection = db_connection

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
        return self._db_connection.execute(
            """SELECT shortcode FROM url WHERE shortcode=%s;""",
            (short_code,)
        )
    
    def create_short_url(self, long_url: str, short_code: str) -> Any:
        """
        Creates a new short URL mapping in the database.

        Args:
            long_url (str): the original long URL.
            short_code (str): the generated short code.

        Returns:
            Any: query result of the insert operation.
        """
        return self._db_connection.execute(
            """INSERT INTO url(shortcode, long_url, created_at) 
               VALUES (%s, %s, toTimestamp(now())) IF NOT EXISTS;""",
            (short_code, long_url)
        )
    
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
        return self._db_connection.execute(
            """
                SELECT long_url FROM url 
                WHERE shortcode=%s;
            """, (short_code,)
        )
