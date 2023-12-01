from flask import g, request, Flask
from passlib.context import CryptContext

from memories.adapters import identity_provider


class IdentityProviderMiddleware:
    def __init__(self, app: Flask):
        app.before_request(self.open)

    def open(self):
        auth_string = request.headers.get("Authorization", default="")
        g.identity_provider = identity_provider.BasicIdentityProvider(
            auth_string, g.session, CryptContext(schemes=["bcrypt"])
        )
