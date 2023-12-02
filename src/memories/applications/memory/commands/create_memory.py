from memories.applications.common.interfaces import IdentityProvider
from memories.applications.common.exceptions import ApplicationException

from memories.domain.memory import value_objects, models
from memories.applications.memory.interfaces import MemoryUnitOfWork
from memories.applications.memory.models import command


class CreateMemoryCommand:
    def __init__(
        self,
        identity_provider: IdentityProvider,
        uow: MemoryUnitOfWork,
    ):
        self._identity_provider = identity_provider
        self._uow = uow

    def __call__(self, command_data: command.CreateMemory) -> int:
        user_id = self._identity_provider.identify()

        title = value_objects.text_block.Title(command_data.title)
        text = value_objects.text_block.Text(command_data.text)
        photo = value_objects.media.Photo(command_data.photo)

        memory = models.Memory(title, text, photo, user_id)

        try:
            memory_id = self._uow.memory_repo.create_memory(memory)
            self._uow.commit()
        except ApplicationException as exc:
            self._uow.rollback()
            raise exc

        return memory_id
