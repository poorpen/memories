from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from memories.applications.common.interfaces import UnitOfWork
from memories.applications.memory.interfaces import MemoryUnitOfWork
from memories.applications.user.interfaces import UserUnitOfWork

from memories.adapters.database.repositories import user, memory
from memories.adapters.database import exceptions


class UnitOfWorkImpl(UnitOfWork, MemoryUnitOfWork, UserUnitOfWork):
    def __init__(self, session: Session):
        self._session = session
        self.memory_repo = memory.MemoryRepoImpl(self._session)
        self.memory_reader = memory.MemoryReaderImpl(self._session)
        self.user_repo = user.UserRepoImpl(self._session)

    def commit(self) -> None:
        try:
            self.commit()
        except SQLAlchemyError as exc:
            raise exceptions.CommitError from exc

    def rollback(self) -> None:
        try:
            self.rollback()
        except SQLAlchemyError as exc:
            raise exceptions.RollbackError from exc
