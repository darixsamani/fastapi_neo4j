from neontology import init_neontology, Neo4jConfig
from config.config import settings



print("samani", settings.neo4j_uri, settings.neo4j_username, settings.neo4j_password)

config = Neo4jConfig(
    uri=settings.neo4j_uri, 
    username=settings.neo4j_username,
    password=settings.neo4j_password
)


def initiate_database():
    
    init_neontology(config)