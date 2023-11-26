from dataclasses import dataclass


@dataclass
class CreateMemory:
    title: str
    text: str
    photo: str


@dataclass
class UpdateMedia:
    memory_id: int
    photo_url: str


@dataclass
class UpdateText:
    memory_id: int
    title: str
    text: str


@dataclass
class DeleteMemory:
    memory_id: int
