from typing import Tuple, Optional
from base64 import b64decode

from passlib.context import CryptContext
from sqlalchemy import select, RowMapping
from sqlalchemy.orm import Session

from memories.applications.common.interfaces import IdentityProvider
from memories.applications.common.exceptions import ApplicationException, AccessDenied
from memories.adapters.database.models.user import user


class AuthStringError(ApplicationException):
    pass


class MissingEmailOrPassword(ApplicationException):
    pass


class MissingBasic(ApplicationException):
    pass


class BasicIdentityProvider(IdentityProvider):
    def __init__(self, auth_string: str, session: Session, hasher: CryptContext):
        self._session = session
        self._auth_string = auth_string
        self._hasher = hasher

    def identify(self) -> int:
        email, password = self._decode_string()
        user_data = self._get_user(email)
        if user_data and self._hasher.verify(password, user_data["password"]):
            return user_data["id"]
        raise AccessDenied()

    def _decode_string(self) -> Tuple[str, str]:
        split_string = self._auth_string.strip().split(" ")

        if split_string[0].lower() != "basic":
            raise MissingBasic()

        try:
            email, password = b64decode(split_string[1]).decode().split(":")
            return email, password
        except ValueError as exc:
            raise MissingEmailOrPassword from exc

    def _get_user(self, email: str) -> Optional[RowMapping]:
        stmt = select(user.c.id, user.c.password).where(user.c.email == email)
        res = self._session.execute(stmt)
        return res.mappings().one_or_none()
