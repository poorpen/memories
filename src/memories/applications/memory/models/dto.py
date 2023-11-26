from dataclasses import dataclass
from datetime import datetime


@dataclass
class Memory:
    id: int
    owner_id: int
    title: str
    photo: str
    deleted: bool
    create_at: datetime


