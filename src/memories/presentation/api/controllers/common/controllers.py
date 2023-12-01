from flask import Flask
from pydantic import ValidationError

from memories import domain, applications
from memories.presentation.api.controllers.common import exception_handlers


def setup_common_exception(app: Flask):
    app.register_error_handler(
        domain.exceptions.DomainException, exception_handlers.exception_handler(400)
    )
    app.register_error_handler(
        applications.exceptions.AuthError, exception_handlers.exception_handler(403)
    )
    app.register_error_handler(
        applications.exceptions.AccessDenied, exception_handlers.exception_handler(403)
    )
    app.register_error_handler(
        ValidationError, exception_handlers.validation_exception_handler
    )
    # app.register_error_handler(
    #     applications.exceptions.UnexpectedAppError,
    #     exception_handlers.exception_handler(500),
    # )
    # app.register_error_handler(Exception, exception_handlers.unknown_exception_handler)
