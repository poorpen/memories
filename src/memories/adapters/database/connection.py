from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from memories.adapters.database.config import DatabaseConfig


def get_database_connections(config: DatabaseConfig) -> sessionmaker:
    engine = create_engine(
        f"{config.drive}://{config.user}:{config.password}@{config.host}:{config.port}/{config.database}"
    )
    return sessionmaker(bind=engine)
