from interfaces import IURLRepository, IDBConnection
from datetime import datetime


class CassandraDBURLRepository(IURLRepository):
    def __init__(self, db_connection: IDBConnection):
        self._db_connection = db_connection

    def create_short_url(self, long_url: str, url_path: str) -> str:
        response = self._db_connection.execute(
            """
                INSERT INTO url(shortcode, long_url, created_at) 
                VALUES (%s, %s, %s);
            """, (url_path, long_url, datetime.now())
        )
        return response

    def get_long_url(self, url_path: str) -> str:
        response = self._db_connection.execute(
            """
                SELECT long_url FROM url 
                WHERE shortcode=%s;
            """, (url_path,)
        )
        return response.one()


if __name__ == "__main__":
    from db_connection import CassandraDBConnection


    url_repository = CassandraDBURLRepository(
        CassandraDBConnection(
            hosts=['0.0.0.0'],
            port=9042,
            keyspace="urls"
        )
    )

    # print(url_repository.create_short_url(
    #     long_url="https://www.youtube.com",
    #     url_path="testtest"
    # ))

    print(url_repository.get_long_url("testtest"))
