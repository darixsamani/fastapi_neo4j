from pydantic import BaseSettings
import os

class Settings(BaseSettings):


    neo4j_uri: str = os.environ.get("NEO4J_URI")
    neo4j_username: str = os.environ.get("NEO4J_USERNAME")
    neo4j_password: str  = os.environ.get("NEO4j_PASSWORD")
    redis_host: str = os.environ.get("REDIS_HOST")
    redis_port: str = os.environ.get("REDIS_PORT")




     # JWT
    secret_key: str = "secret"
    algorithm: str = "HS256"

    class Config:
        env_file = ".env.dev"
        orm_mode = True



settings = Settings()