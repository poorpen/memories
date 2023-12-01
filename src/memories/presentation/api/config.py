import os

from dataclasses import dataclass

from memories.adapters.database.config import DatabaseConfig


@dataclass
class APIConfig:
    host: str
    port: int


@dataclass
class ApplicationConfig:
    api: APIConfig
    database: DatabaseConfig


def load_config() -> ApplicationConfig:
    return ApplicationConfig(
        APIConfig(
            os.environ.get("API_HOST", default="0.0.0.0"),
            os.environ.get("API_PORT", default=8000),
        ),
        DatabaseConfig(
            os.environ["DB_NAME"],
            os.environ["DB_USER"],
            os.environ["DB_PASSWORD"],
            os.environ["DB_HOST"],
            os.environ["DB_PORT"],
            os.environ["DB_DRIVE"],
        ),
    )
