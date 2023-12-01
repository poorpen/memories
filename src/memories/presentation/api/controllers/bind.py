from flask import Flask

from memories.applications import memory
from memories.presentation.api.controllers import memory, user, common


def bind_routers(app: Flask):
    app.register_blueprint(memory.memories_router)
    app.register_blueprint(user.users_router)

    common.setup_common_exception(app)
