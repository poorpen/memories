from pydantic import BaseModel, Field


class AddMemory(BaseModel):
    title: str
    text: str
    photo: str


class UpdateMedia(BaseModel):
    memory_id: int
    photo_url: str


class UpdateText(BaseModel):
    memory_id: int
    title: str
    text: str


class GetMemories(BaseModel):
    limit: int = Field(default=10)
    offset: int = Field(default=0)
