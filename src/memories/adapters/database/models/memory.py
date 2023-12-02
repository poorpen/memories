from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Boolean,
)
from sqlalchemy.orm import composite

from memories.domain.memory import models
from memories.domain.memory.value_objects import text_block, media
from memories.adapters.database.models.base import metadata_obj, mapper_registry


memory = Table(
    "memories",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("title", String(60), nullable=False),
    Column("text", String(3000), nullable=False),
    Column("photo", String, nullable=True),
    Column("owner_id", Integer, ForeignKey("users.id")),
    Column("deleted", Boolean, nullable=False),
    Column("create_at", DateTime, nullable=False),
    Column("update_at", DateTime, nullable=False),
)


def map_memory() -> None:
    mapper_registry.map_imperatively(
        models.Memory,
        memory,
        properties={
            "id": memory.c.id,
            "title": composite(text_block.Title, memory.c.title),
            "text": composite(text_block.Text, memory.c.text),
            "photo": composite(media.Photo, memory.c.photo),
            "deleted": memory.c.deleted,
            "create_at": memory.c.create_at,
            "update_at": memory.c.update_at,
            "owner_id": memory.c.owner_id,
        },
        column_prefix="_",
    )
