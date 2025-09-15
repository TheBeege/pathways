from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 9080
