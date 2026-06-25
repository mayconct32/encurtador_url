import os
from functools import lru_cache
from dotenv import load_dotenv
from fastapi import Depends
from db_connection import CassandraDBConnection
from repository import CassandraDBURLRepository
from service import URLService
from interfaces import IDBConnection, IURLRepository


load_dotenv()

@lru_cache(maxsize=1)
def get_connection_db() -> IDBConnection:
    hosts = os.getenv("HOSTS")
    port = os.getenv("PORT")
    keyspace = os.getenv("KEYSPACE")
    if not all([hosts, port, keyspace]):
        raise ValueError("HOSTS, PORT, and KEYSPACE variables not found in .env")
    return CassandraDBConnection(hosts, port, keyspace)  


def get_url_repository(
    connection: IDBConnection = Depends(get_connection_db)  
) -> IURLRepository:  
    return CassandraDBURLRepository(connection)


def get_url_service(
    repository: IURLRepository = Depends(get_url_repository)  
) -> URLService: 
    return URLService(repository)