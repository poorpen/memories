from memories.applications.common.interfaces import UnitOfWork
from memories.applications.memory.interfaces import MemoryRepo, MemoryReader


class MemoryUnitOfWork(UnitOfWork):
    memory_repo: MemoryRepo
    memory_reader: MemoryReader
