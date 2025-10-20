import logging
from pydantic_settings import BaseSettings, SettingsConfigDict


# This Settings class automatically retrieves environment variables and stores them
# in these class variables. Environment variable names are expected to be in all caps.
# Type validation is done automatically.
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    environment: str = "DEV"
    public_base_url: str = "http://localhost:5000"
    host_address: str = "0.0.0.0"
    port: int = 5000
    graphdb_host: str = "graphdb"
    graphdb_port: int = "9080"
    graphdb_username: str = "root"
    graphdb_password: str = "root"
    graphdb_database: str = "pathways"
    log_level: str = "INFO"
    seed_data: bool = False

    def get_graphdb_url(self):
        # return "dgraph://{user}:{password}@{host}:{port}".format(
        return "dgraph://{host}:{port}".format(
            # user=self.graphdb_username,
            # password=self.graphdb_password,
            host=self.graphdb_host,
            port=self.graphdb_port,
        )
