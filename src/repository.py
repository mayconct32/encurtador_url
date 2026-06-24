from interfaces import IURLRepository, IDBConnection
from typing import Any


class CassandraDBURLRepository(IURLRepository):
    def __init__(self, db_connection: IDBConnection) -> None:
        self._db_connection = db_connection

    def get_short_url(self, short_code: str) -> Any:
        return self._db_connection.execute(
            """SELECT shortcode FROM url WHERE shortcode=%s;""",
            (short_code,)
        )
    
    def create_short_url(self, long_url: str, short_code: str) -> Any:
        return self._db_connection.execute(
            """INSERT INTO url(shortcode, long_url, created_at) 
               VALUES (%s, %s, toTimestamp(now())) IF NOT EXISTS;""",
            (short_code, long_url)
        )
    
    def get_long_url(self, short_code: str) -> Any:
        return self._db_connection.execute(
            """
                SELECT long_url FROM url 
                WHERE shortcode=%s;
            """, (short_code,)
        )
