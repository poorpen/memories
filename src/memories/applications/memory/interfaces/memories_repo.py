from typing import Protocol

from memories.domain.memory.models import Memory


class MemoriesRepo(Protocol):
    def create_memory(self, memory: Memory) -> int:
        raise NotImplemented

    def update_memory(self, memory: Memory) -> None:
        raise NotImplemented

    def get_memory(self, memory_id: int) -> Memory:
        raise NotImplemented
