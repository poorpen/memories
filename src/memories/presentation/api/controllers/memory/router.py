from flask import Blueprint

from memories.presentation.api.controllers.common import exception_handlers

from memories.applications.memory import exceptions


memories_router = Blueprint("memories", __name__, url_prefix="/memories")

memories_router.register_error_handler(
    exceptions.MemoryNotExist, exception_handlers.exception_handler(404)
)