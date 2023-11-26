from dataclasses import dataclass
from email_validator import validate_email, EmailNotValidError

from memories.domain.common.exceptions import DomainException
from memories.domain.common.value_objects.base import SingleValueObject


class InvalidEmailAddress(DomainException):
    @property
    def message(self) -> str:
        return "Email address has invalid format"


@dataclass(frozen=True)
class EmailAddress(SingleValueObject[str]):
    value: str

    def _validate(self) -> None:
        try:
            validate_email(self.value)
        except EmailNotValidError:
            raise InvalidEmailAddress()


@dataclass(frozen=True)
class Password(SingleValueObject[str]):
    value: str
