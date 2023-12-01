from functools import partial

from memories import domain
from memories.presentation.api.controllers.common import responses


def handle_app_exception(exc: domain.exceptions.AppException, code: int):
    return (
        responses.ExceptionModel(
            message=exc.message, type=exc.exception_type
        ).model_dump_json(),
        code,
    )


def handle_unknown_exception(exc: Exception, code: int):
    return (
        responses.ExceptionModel(
            message="Unknown error has occurred", type="UnexpectedError"
        ).model_dump_json(),
        code,
    )


def exception_handler(code: int):
    return partial(handle_app_exception, code=code)


def unknown_exception_handler(code: int):
    return partial(handle_unknown_exception, code=code)
