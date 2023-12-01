from datetime import datetime

from pydantic import BaseModel, Field


class Memory(BaseModel):
    id: int
    title: str
    text: str
    photo: str
    owner_id: int
    create_at: datetime
    update_at: datetime


class MemoryId(BaseModel):
    id: int
