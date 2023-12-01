from flask import g, Flask

from sqlalchemy.orm import sessionmaker

from memories.adapters.database.uow import UnitOfWorkImpl
from memories.adapters.database.repositories.permission import PermissionsGatewayImpl


class DatabaseMiddleware:
    def __init__(self, app: Flask, session_maker: sessionmaker):
        self.session_maker = session_maker

        app.before_request(self.open)
        app.teardown_appcontext(self.close)

    def open(self) -> None:
        session = self.session_maker()
        g.session = session
        g.uow = UnitOfWorkImpl(session)
        g.permissions_gateway = PermissionsGatewayImpl(session)

    def close(self, *args, **kwargs):
        g.session.close()
