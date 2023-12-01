from datetime import datetime

from pydantic import BaseModel, Field


class Memory(BaseModel):
    id: int
    title: str
    text: str
    photo: str
    owner_id: int = Field(alias="ownerID")
    create_at: datetime = Field(alias="createAt")
    update_at: datetime = Field(alias="updateAt")


class MemoryId(BaseModel):
    id: int
