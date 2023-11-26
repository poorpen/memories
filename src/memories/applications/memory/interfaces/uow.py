from memories.applications.common.interfaces.uow import UnitOfWork
from memories.applications.memory.interfaces import memories_repo, memories_reader


class MemoriesUnitOfWork(UnitOfWork):
    memories_repo: memories_repo.MemoriesRepo
    memories_reader: memories_reader.MemoriesReader
