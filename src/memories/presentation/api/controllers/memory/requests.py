from pydantic import BaseModel, Field, model_validator
from pydantic_core import PydanticCustomError


class AddMemory(BaseModel):
    title: str
    text: str
    photo: str


class UpdateMedia(BaseModel):
    photo: str


class UpdateText(BaseModel):
    title: str = None
    text: str = None

    @model_validator(mode="after")
    def check_all_empty(self) -> "UpdateText":
        if not self.title and not self.text:
            raise PydanticCustomError(
                "values_is_empty",
                "all fields is empty",
                dict(wrong_value=None),
            )
        return self


class GetMemories(BaseModel):
    limit: int = Field(default=10)
    offset: int = Field(default=0)
