from dataclasses import dataclass


@dataclass
class MemoryQuery:
    limit: int
    offset: int


class GetMyMemories(MemoryQuery):
    pass


class GetOtherMemories(MemoryQuery):
    pass
