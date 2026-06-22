from interfaces import IURLRepository, IDBConnection


class CassandraDBURLRepository(IURLRepository):
    def __init__(self, db_connection: IDBConnection):
        self._db_connection = db_connection

    def create_short_url(self, long_url: str, url_path: str) -> str:
        pass

    def get_long_url(self, url_path: str) -> str:
        pass

