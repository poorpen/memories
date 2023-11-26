from dataclasses import dataclass


@dataclass
class RegisterUser:
    email_address: str
    password: str
