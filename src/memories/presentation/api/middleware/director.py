from flask import g, Flask

from memories.domain.user.services import PasswordHasher
from memories.applications import user, memory
from memories.adapters.director import Director


class DirectorMiddleware:
    def __init__(self, app: Flask):
        app.before_request(self.open)

    def open(self):
        director = Director()

        identity_provider = g.identity_provider
        uow = g.uow

        director.register_handler(
            memory.models.command.CreateMemory,
            memory.commands.CreateMemoryCommand(
                identity_provider, uow
            ),
        )
        director.register_handler(
            memory.models.command.UpdateText,
            memory.commands.UpdateMemoryText(
                identity_provider, uow
            ),
        )
        director.register_handler(
            memory.models.command.UpdateMedia,
            memory.commands.UpdateMemoryMedia(
                identity_provider, uow
            ),
        )
        director.register_handler(
            memory.models.command.DeleteMemory,
            memory.commands.DeleteMemory(identity_provider, uow),
        )
        director.register_handler(
            memory.models.query.GetMyMemories,
            memory.queries.GetMyMemories(identity_provider, uow),
        )
        director.register_handler(
            memory.models.query.GetOtherMemories,
            memory.queries.GetOtherMemories(identity_provider, uow),
        )
        director.register_handler(
            user.models.command.RegisterUser, user.commands.RegisterUser(uow, PasswordHasher(g.hasher))
        )

        g.director = director
