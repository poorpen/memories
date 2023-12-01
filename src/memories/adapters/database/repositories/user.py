from sqlalchemy.exc import IntegrityError

from memories.domain.user.models import User
from memories.applications.user.exceptions import UserAlreadyExist
from memories.applications.user.interfaces.user_repo import UserRepo
from memories.adapters.database import exception_mapper, models
from memories.adapters.database.repositories.base import SQLAlchemyRepo


class UserRepoImpl(SQLAlchemyRepo, UserRepo):
    @exception_mapper
    def add_user(self, user: User) -> None:
        self._session.add(user)
        try:
            self._session.flush()
        except IntegrityError as exc:
            match exc.__cause__.__cause__.constraint_name:
                case "pk_users":
                    raise UserAlreadyExist()
