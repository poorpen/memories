from typing import Sequence, List, Optional

from sqlalchemy import RowMapping

from memories.applications.common.models import dto


def to_dto(data: RowMapping) -> dto.Permission:
    return dto.Permission(**data)


def to_dtos(data: Sequence[RowMapping]) -> List[Optional[dto.Permission]]:
    return [to_dto(row) for row in data]
