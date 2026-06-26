from typing import Any
from cassandra.cluster import Cluster
from interfaces import IDBConnection


class CassandraDBConnection(IDBConnection):
    """
    Class responsible for the connection to the 
    Cassandra database.
    """
    def __init__(self, hosts: list, port: int, keyspace: str) -> None:
        """
        Initializes the Cassandra database connection.

        Args:
            hosts (list): list of database host addresses.
            port (int): database connection port.
            keyspace (str): the Cassandra keyspace to use.

        Returns:
            None
        """
        self._cluster = Cluster(hosts, port=port)
        self._session = self._cluster.connect(keyspace)

    @property
    def session(self) -> Any:
        """
        Returns the active Cassandra session.

        Returns:
            Any: the Cassandra session object.
        """
        return self._session
    
    def execute(self, query: str, params: Any = None) -> Any:
        """
        Executes a CQL query with optional parameters.

        Args:
            query (str): the CQL query to execute.
            params (Any): optional query parameters.

        Returns:
            Any: query result.
        """
        return self._session.execute(query, params)

    def shutdown(self) -> None:
        """
        Shuts down the Cassandra cluster connection.

        Returns:
            None
        """
        self._cluster.shutdown()
