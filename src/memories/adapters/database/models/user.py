from sqlalchemy import Table, Column, Integer, String


from memories.domain.user.models import User
from memories.adapters.database.models.base import metadata_obj, mapper_registry

user = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("password", String, nullable=False),
)


def map_user() -> None:
    mapper_registry.map_imperatively(User, user)
