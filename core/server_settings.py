from typing import Optional

from pydantic.v1 import BaseSettings


class ServerSettings(BaseSettings):
    app_name: str = "langserve-base"
    app_host: str = "0.0.0.0"
    app_port: int = 8000

    elasticsearch_url: Optional[str] = "http://elasticsearch.ops-pilot:9200"
    elasticsearch_password: Optional[str]

    class Config:
        env_file = ".env"


server_settings = ServerSettings()
