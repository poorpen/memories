from typing import List, Optional

from sqlalchemy import select

from memories.applications.memory.models import dto
from memories.domain.memory.models import Memory
from memories.applications.memory.exceptions import MemoryNotExist
from memories.applications.memory.interfaces import MemoryRepo, MemoryReader
from memories.adapters.database import exception_mapper, models, converters
from memories.adapters.database.repositories.base import SQLAlchemyRepo


class MemoryRepoImpl(SQLAlchemyRepo, MemoryRepo):
    @exception_mapper
    def create_memory(self, memory: Memory) -> int:
        self._session.add(memory)
        self._session.flush()
        return memory.id

    @exception_mapper
    def update_memory(self, memory: Memory) -> None:
        self._session.merge(memory)

    @exception_mapper
    def get_memory(self, memory_id: int) -> Memory:
        stmt = select(Memory).where(Memory.id == memory_id)
        res = self._session.execute(stmt)
        memory = res.scalar()
        if memory is None:
            raise MemoryNotExist()

        return memory


class MemoryReaderImpl(SQLAlchemyRepo, MemoryReader):
    def get_memories_by_user_id(
        self, user_id: int, limit: int, offset: int
    ) -> List[Optional[dto.Memory]]:
        stmt = (
            select(*filter(lambda c: c.name != "deleted", models.memory.c))
            .offset(offset)
            .limit(limit)
            .where(models.memory.c.owner_id == user_id)
            .where(models.memory.c.deleted is False)
        )

        res = self._session.execute(stmt)
        mapped_res = res.mappings().all()
        return converters.memory.to_dtos(mapped_res)

    def get_other_memories(
        self, user_id: int, limit: int, offset: int
    ) -> List[Optional[dto.Memory]]:
        stmt = (
            select(*filter(lambda c: c.name != "deleted", models.memory.c))
            .offset(offset)
            .limit(limit)
            .where(models.memory.c.owner_id != user_id)
            .where(models.memory.c.deleted is False)
        )

        res = self._session.execute(stmt)
        mapped_res = res.mappings().all()
        return converters.memory.to_dtos(mapped_res)
