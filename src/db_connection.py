from typing import Any
from cassandra.cluster import Cluster


class CassandraDBConnection():
    def __init__(self, hosts: list, port: int, keyspace: str) -> None:
        self._cluster = Cluster(hosts, port=port)
        self._session = self._cluster.connect(keyspace)

    @property
    def session(self) -> Any:
        return self._session
    
    def execute(self, query: str, params: Any = None) -> Any:
        return self._session.execute(query, params)

    def shutdown(self) -> None:
        self._cluster.shutdown()
