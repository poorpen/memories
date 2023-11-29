from flask import g, request
from passlib.context import CryptContext

from memories.adapters import identity_provider


class IdentityProviderMiddleware:
    def __call__(self):
        auth_string = request.headers.get("Authorization")
        g.identity_provider = identity_provider.BasicIdentityProvider(
            auth_string, g.session, CryptContext(schemes=["bcrypt"])
        )
