from pydantic import BaseModel


class RegisterUser(BaseModel):
    email_address: str
    password: str

