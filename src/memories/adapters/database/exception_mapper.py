from typing import Callable, Any
from sqlalchemy.exc import SQLAlchemyError

from memories.applications.common.exceptions import RepoError


def exception_mapper(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapped(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as err:
            raise RepoError from err

    return wrapped
