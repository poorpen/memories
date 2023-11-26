import pytest
import faker
from passlib.context import CryptContext

from memories.domain.user.value_objects import credentials
from memories.domain.user.services import password_hasher


def test_password_hash():
    fake = faker.Faker()
    password = fake.word()
    crypt_context = CryptContext(schemes=["bcrypt"])
    hasher = password_hasher.PasswordHasher(crypt_context)
    assert crypt_context.verify(password, hasher.hash_password(password).raw_value)
