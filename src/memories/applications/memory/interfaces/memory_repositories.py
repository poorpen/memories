from typing import Protocol, Optional, List

from memories.domain.memory.models import Memory
from memories.applications.memory.models import dto


class MemoryRepo(Protocol):
    def create_memory(self, memory: Memory) -> int:
        raise NotImplemented

    def update_memory(self, memory: Memory) -> None:
        raise NotImplemented

    def get_memory(self, memory_id: int) -> Memory:
        raise NotImplemented


class MemoryReader(Protocol):
    def get_memories_by_user_id(
        self, user_id: int, limit: int, offset: int
    ) -> List[Optional[dto.Memory]]:
        raise NotImplemented

    def get_other_memories(
        self, excluded_user_id: int, limit: int, offset: int
    ) -> List[Optional[dto.Memory]]:
        raise NotImplemented
