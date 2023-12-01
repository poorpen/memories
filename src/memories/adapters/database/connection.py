from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from memories.adapters.database.config import DatabaseConfig
from memories.adapters.database.models.map import register_all_maps


def get_database_connection(config: DatabaseConfig) -> sessionmaker:
    engine = create_engine(
        f"{config.drive}://{config.user}:{config.password}@{config.host}:{config.port}/{config.database}"
    )
    register_all_maps()
    return sessionmaker(bind=engine)
