from typing import Protocol, List, Optional

from memories.applications.common.models import dto


class PermissionsGateway(Protocol):
    def get_for_memories(
        self, user_id: int, memory_id: int
    ) -> List[Optional[dto.Permission]]:
        raise NotImplemented

    def add_for_memories(
        self, user_id: int, memory_id: int, permissions: List[dto.Permission]
    ) -> None:
        raise NotImplemented
