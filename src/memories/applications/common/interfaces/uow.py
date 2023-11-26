from typing import Protocol


class UnitOfWork(Protocol):
    def commit(self) -> None:
        raise NotImplemented

    def rollback(self) -> None:
        raise NotImplemented
