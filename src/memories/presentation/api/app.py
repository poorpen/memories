from flask import Flask
from swagger_ui import api_doc

from memories.adapters.database.connection import get_database_connection
from memories.presentation.api.middleware import bind_middleware
from memories.presentation.api.controllers import bind_routers
from memories.presentation.api.config import ApplicationConfig


def build_app(config: ApplicationConfig) -> Flask:
    app = Flask("memories")

    database_connection = get_database_connection(config.database)

    bind_middleware(app, database_connection)
    bind_routers(app)

    api_doc(app, config_path='memories.yml', url_prefix="/docs", title="Memories docs")
    return app
