from sqlalchemy.orm import Session


class SQLAlchemyRepo:
    def __init__(self, session: Session):
        self._session = session
