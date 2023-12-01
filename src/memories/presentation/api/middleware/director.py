from flask import g, Flask

from memories.applications.memory import models, commands, queries
from memories.adapters.director import Director


class DirectorMiddleware:
    def __init__(self, app: Flask):
        app.before_request(self.open)

    def open(self):
        director = Director()

        identity_provider = g.identity_provider
        permissions_gateway = g.permissions_gateway
        uow = g.uow

        director.register_handler(
            models.command.CreateMemory,
            commands.CreateMemoryCommand(identity_provider, permissions_gateway, uow),
        )
        director.register_handler(
            models.command.UpdateText,
            commands.UpdateMemoryText(identity_provider, permissions_gateway, uow),
        )
        director.register_handler(
            models.command.UpdateMedia,
            commands.UpdateMemoryMedia(identity_provider, permissions_gateway, uow),
        )
        director.register_handler(
            models.command.DeleteMemory,
            commands.DeleteMemory(identity_provider, permissions_gateway, uow),
        )
        director.register_handler(
            models.query.GetMyMemories, queries.GetMyMemories(identity_provider, uow)
        )
        director.register_handler(
            models.query.GetOtherMemories,
            queries.GetOtherMemories(identity_provider, uow),
        )

        g.director = director
