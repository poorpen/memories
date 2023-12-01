from flask import Flask
from sqlalchemy.orm import sessionmaker

from memories.presentation.api import middleware


def bind_middleware(app: Flask, session_maker: sessionmaker) -> None:
    middleware.DatabaseMiddleware(app, session_maker)
    middleware.IdentityProviderMiddleware(app)
    middleware.DirectorMiddleware(app)
