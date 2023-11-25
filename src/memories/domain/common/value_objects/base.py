from dataclasses import dataclass
from typing import Any, TypeVar, Generic

T = TypeVar("T", bound=Any)


@dataclass(frozen=True)
class ValueObject:

    def _validate(self) -> None:
        """
        This method checks that value is valid
        :return: None
        """
        raise NotImplemented

    def __post_init__(self) -> None:
        self._validate()


@dataclass(frozen=True)
class SingleValueObject(ValueObject, Generic[T]):
    value: T

    @property
    def raw_value(self) -> T:
        return self.value
