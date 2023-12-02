from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class Memory(BaseModel):
    id: int
    title: str
    text: str
    photo: str
    owner_id: int = Field(alias="ownerID")
    create_at: datetime = Field(alias="createAt")
    update_at: datetime = Field(alias="updateAt")

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}
        populate_by_name = True


class MemoryId(BaseModel):
    id: int
