from dataclasses import dataclass

from memories.domain.common.exceptions import DomainException
from memories.domain.common.value_objects.base import SingleValueObject


class StringIsEmpty(DomainException):
    @property
    def message(self) -> str:
        return "Submitted string is empty or contains only spaces"


class CharacterLimitExceeded(DomainException):
    @property
    def message(self) -> str:
        return "Length of the string exceeds the allowed number of characters"


@dataclass(frozen=True)
class NonEmptyString(SingleValueObject[str]):
    value: str
    max_len: int

    def _validate(self) -> None:
        if not self.value or self.value.isspace():
            raise StringIsEmpty()
        elif len(self.value) >= self.max_len:
            raise CharacterLimitExceeded()


@dataclass(frozen=True)
class Title(NonEmptyString):
    max_len: int = 60


@dataclass(frozen=True)
class Text(NonEmptyString):
    max_len: int = 3000
