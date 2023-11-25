import validators

from dataclasses import dataclass

from memories.domain.common.exceptions import DomainException
from memories.domain.common.value_objects.base import ValueObject


class InvalidPhotoURL(DomainException):
    @property
    def message(self) -> str:
        return "Submitted url has an invalid format"


@dataclass(frozen=True)
class Photo(ValueObject):
    photo_url: str

    def _validate(self) -> None:
        if not validators.url(self.photo_url):
            raise InvalidPhotoURL()

    @property
    def raw_value(self) -> str:
        return self.photo_url
