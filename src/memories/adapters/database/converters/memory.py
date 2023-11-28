from typing import List, Sequence

from sqlalchemy import RowMapping

from memories.applications.memory.models import dto


def to_dto(data: RowMapping) -> dto.Memory:
    return dto.Memory(**data)


def to_dtos(data: Sequence[RowMapping]) -> List[dto.Memory]:
    return [to_dto(row) for row in data]
