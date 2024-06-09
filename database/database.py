from neontology import init_neontology
from config.config import settings



def initiate_database():

    init_neontology(
    neo4j_uri = settings.neo4j_uri,
    neo4j_username = settings.neo4j_username,
    neo4j_password = settings.neo4j_password,
    )