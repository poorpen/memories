from pydantic import BaseModel


class ExceptionModel(BaseModel):
    message: str
    type: str
