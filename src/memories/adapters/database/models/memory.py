from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Boolean,
    Enum,
)
from memories.domain.memory import models
from memories.applications.common.models import dto
from memories.applications.common.constants import PermissionType
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

permissions_for_memory = Table(
    "permissions_for_memory",
    metadata_obj,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("memory_id", Integer, ForeignKey("memories.id"), primary_key=True),
    Column("permission_type", Enum(PermissionType), nullable=False),
    Column("allowed", Boolean, nullable=False),
)


def map_memory() -> None:
    mapper_registry.map_imperatively(models.Memory, memory)
    mapper_registry.map_imperatively(dto.Permission, permissions_for_memory)
