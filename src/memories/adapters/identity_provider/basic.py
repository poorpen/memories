from typing import Tuple, Optional
from base64 import b64decode

from passlib.context import CryptContext
from sqlalchemy import select, RowMapping
from sqlalchemy.orm import Session

from memories.applications.common.interfaces import IdentityProvider
from memories.applications.common.exceptions import ApplicationException, AccessDenied
from memories.adapters.database.models.user import user


class MissingEmailOrPassword(ApplicationException):
    @property
    def message(self) -> str:
        return "Password or name has been omitted from the authentication string"


class MissingBasic(ApplicationException):
    @property
    def message(self) -> str:
        return 'The word "basic" is missing from the authentication string'


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

        if not split_string or split_string[0].lower() != "basic":
            raise MissingBasic()

        try:
            email, password = b64decode(split_string[1]).decode().split(":")
            return email, password
        except (ValueError, IndexError) as exc:
            raise MissingEmailOrPassword from exc

    def _get_user(self, email: str) -> Optional[RowMapping]:
        stmt = select(user.c.id, user.c.password).where(user.c.email == email)
        res = self._session.execute(stmt)
        return res.mappings().one_or_none()
