import os

from memories.presentation.api import build_app, load_config


if __name__ == "__main__":
    config = load_config()
    app = build_app(config)
    app.run(host=config.api.host, port=config.api.port)
