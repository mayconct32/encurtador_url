from cassandra.cluster import Cluster


class CassandraConnection:
    def __init__(self, hosts, port, keyspace):
        self._cluster = Cluster(hosts, port=port)
        self._session = self._cluster.connect(keyspace)

    @property
    def session(self):
        return self._session

    def execute(self, query, params=None):
        return self._session.execute(query, params)

    def shutdown(self):
        self._cluster.shutdown()
