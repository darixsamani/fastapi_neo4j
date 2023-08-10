from neontology import init_neontology
from config.config import settings
from neo4j import GraphDatabase
from redis import Redis


def initiate_database():

    init_neontology(
    neo4j_uri = settings.neo4j_uri,
    neo4j_username = settings.neo4j_username,
    neo4j_password = settings.neo4j_password,
    )

AUTH_NEO4j = (settings.neo4j_username,settings.neo4j_password)

driver =  GraphDatabase.driver(settings.neo4j_uri, auth=AUTH_NEO4j )

redis = Redis(host=settings.redis_host, port=settings.redis_port)