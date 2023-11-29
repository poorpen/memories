from flask import g

from sqlalchemy.orm import sessionmaker

from memories.adapters.database.uow import UnitOfWorkImpl
from memories.adapters.database.repositories.permission import PermissionsGatewayImpl


class DatabaseMiddleware:
    def __init__(self, session_maker: sessionmaker):
        self.session_maker = session_maker

    def __call__(self) -> None:
        with self.session_maker() as session:
            g.session = session
            g.uow = UnitOfWorkImpl(session)
            g.permissions_gateway = PermissionsGatewayImpl(session)
            yield
