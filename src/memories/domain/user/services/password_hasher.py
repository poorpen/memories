from passlib.context import CryptContext

from memories.domain.user.value_objects import credentials


class PasswordHasher:
    def __init__(self, hasher: CryptContext):
        self._hasher = hasher

    def hash_password(self, password: str) -> credentials.Password:
        return credentials.Password(self._hasher.hash(password))
