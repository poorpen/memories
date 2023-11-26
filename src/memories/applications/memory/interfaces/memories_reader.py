from typing import Protocol, Optional, List

from memories.applications.memory import models


class MemoriesReader(Protocol):
    def get_memories_by_user_id(
        self, user_id: int, limit: int, offset: int
    ) -> List[Optional[models.dto.Memory]]:
        raise NotImplemented

    def get_other_memories(
        self, excluded_user_id: int, limit: int, offset: int
    ) -> List[Optional[models.dto.Memory]]:
        raise NotImplemented
