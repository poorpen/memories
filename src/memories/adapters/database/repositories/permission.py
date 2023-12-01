from typing import List, Optional

from sqlalchemy import select, insert

from memories.applications.common.interfaces.permission_gateway import (
    PermissionsGateway,
)

from memories.applications.common.models import dto
from memories.adapters.database.models.memory import permissions_for_memory
from memories.adapters.database.repositories.base import SQLAlchemyRepo
from memories.adapters.database.converters.permission import to_dtos
from memories.adapters.database.exception_mapper import exception_mapper


class PermissionsGatewayImpl(SQLAlchemyRepo, PermissionsGateway):
    @exception_mapper
    def get_for_memory(
        self, user_id: int, memory_id: int
    ) -> List[Optional[dto.Permission]]:
        stmt = (
            select(permissions_for_memory.c.type, permissions_for_memory.c.allowed)
            .where(permissions_for_memory.c.memory_id == memory_id)
            .where(permissions_for_memory.c.user_id == user_id)
        )

        res = self._session.execute(stmt)

        mapped_res = res.mappings().all()



        return to_dtos(mapped_res)

    @exception_mapper
    def add_for_memory(
        self, user_id: int, memory_id: int, permissions: List[dto.Permission]
    ) -> None:
        for permission in permissions:
            stmt = insert(permissions_for_memory).values(
                user_id=user_id,
                memory_id=memory_id,
                type=permission.type,
                allowed=permission.allowed,
            )
            self._session.execute(stmt)
