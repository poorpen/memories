from typing import List, Optional

from memories.applications.common.interfaces import IdentityProvider

from memories.applications.memory.interfaces import MemoryUnitOfWork
from memories.applications.memory.models import query, dto


class GetOtherMemories:
    def __init__(self, identity_provider: IdentityProvider, uow: MemoryUnitOfWork):
        self._identity_provider = identity_provider
        self._uow = uow

    def __call__(self, query_data: query.GetMyMemories) -> List[Optional[dto.Memory]]:
        user_id = self._identity_provider.identify()
        memories = self._uow.memory_reader.get_other_memories(
            user_id, query_data.limit, query_data.offset
        )
        return memories
