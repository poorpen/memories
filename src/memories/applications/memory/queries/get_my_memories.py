from typing import List, Optional

from memories.applications.common.interfaces import IdentityProvider

from memories.applications.memory.interfaces import MemoriesUnitOfWork
from memories.applications.memory.models import query, dto


class GetMyMemories:
    def __init__(self, identity_provider: IdentityProvider, uow: MemoriesUnitOfWork):
        self._identity_provider = identity_provider
        self._uow = uow

    def __call__(self, query_data: query.GetMyMemories) -> List[Optional[dto.Memory]]:
        user_id = self._identity_provider.identify()
        memories = self._uow.memories_reader.get_memories_by_user_id(
            user_id, query_data.limit, query_data.offset
        )
        return memories
