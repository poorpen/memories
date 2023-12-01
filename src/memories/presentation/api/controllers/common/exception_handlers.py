import json
from functools import partial
from pydantic import ValidationError

from memories import domain
from memories.presentation.api.controllers.common import responses


def handle_app_exception(exc: domain.exceptions.AppException, code: int):
    return (
        responses.ExceptionModel(
            message=exc.message, type=exc.exception_type
        ).model_dump_json(),
        code,
    )


def unknown_exception_handler(exc: Exception):
    return (
        responses.ExceptionModel(
            message="Unknown error has occurred", type="UnexpectedError"
        ).model_dump_json(),
        500,
    )


def validation_exception_handler(exc: ValidationError):
    exc_data = json.loads(exc.json())[0]
    return (
        responses.ExceptionModel(
            message=f'{exc_data["loc"][0]}: {exc_data["msg"]}', type="ValidationError"
        ).model_dump_json(),
        400,
    )


def exception_handler(code: int):
    return partial(handle_app_exception, code=code)
