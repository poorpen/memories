from flask import Flask
from memories.presentation.api.controllers import memory, user


if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(memory.memories_router)
    print(app.url_map)
    app.run()
