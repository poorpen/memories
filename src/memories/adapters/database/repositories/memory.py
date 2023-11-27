from memories.applications.memory.interfaces import MemoryRepo, MemoryReader
from memories.adapters.database import exception_mapper
from memories.adapters.database.repositories.base import SQLAlchemyRepo
from memories.domain.memory.models import Memory


class MemoryRepoImpl(SQLAlchemyRepo, MemoryRepo):

    @exception_mapper
    def create_memory(self, memory: Memory) -> int:
        self._session.add(memory)
        self._session.flush()
        memory_id =  self._session.get(Memory)



class MemoryReaderImpl(SQLAlchemyRepo, MemoryReader):
    pass
