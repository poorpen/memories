from datetime import datetime

from pydantic import BaseModel


class Memory(BaseModel):
    id: int
    owner_id: int
    title: str
    text: str
    photo: str
    create_at: datetime
    update_at: datetime
