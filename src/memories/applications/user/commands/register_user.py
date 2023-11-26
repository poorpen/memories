from memories.applications.common.exceptions import ApplicationException

from memories.domain.user.models import User
from memories.domain.user.value_objects import credentials
from memories.domain.user.services import PasswordHasher

from memories.applications.user.interfaces import UserUnitOfWork
from memories.applications.user.models import command


class RegisterUser:
    def __init__(self, uow: UserUnitOfWork, password_hasher: PasswordHasher):
        self._uow = uow
        self._password_hasher = password_hasher

    def __call__(self, command_data: command.RegisterUser) -> None:
        email = credentials.EmailAddress(command_data.email_address)
        hashed_password = self._password_hasher.hash_password(command_data.password)

        user = User(email, hashed_password)

        try:
            self._uow.user_repo.add_user(user)
            self._uow.commit()
        except ApplicationException as exc:
            self._uow.rollback()
            raise exc
