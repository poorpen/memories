from flask import Flask
from sqlalchemy.orm import sessionmaker

from memories.presentation.api import middleware


def setup_middleware(app: Flask, session_maker: sessionmaker) -> None:
    app.before_request(middleware.DatabaseMiddleware(session_maker))
    app.before_request(middleware.IdentityProviderMiddleware())
    app.before_request(middleware.DirectorMiddleware())
