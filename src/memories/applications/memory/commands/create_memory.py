from memories.applications.common.interfaces import IdentityProvider, PermissionsGateway
from memories.applications.common.models import dto
from memories.applications.common.constants import PermissionType
from memories.applications.common.exceptions import ApplicationException

from memories.domain.memory import value_objects, models
from memories.applications.memory.interfaces import MemoriesUnitOfWork
from memories.applications.memory.models import command


class CreateMemoryCommand:
    def __init__(
        self,
        identity_provider: IdentityProvider,
        permissions_gateway: PermissionsGateway,
        uow: MemoriesUnitOfWork,
    ):
        self._identity_provider = identity_provider
        self._permissions_gateway = permissions_gateway
        self._uow = uow

    def __call__(self, command_data: command.CreateMemory) -> int:
        user_id = self._identity_provider.identify()

        title = value_objects.text_block.Title(command_data.title)
        text = value_objects.text_block.Text(command_data.text)
        photo = value_objects.media.Photo(command_data.photo)

        memory = models.Memory(title, text, photo, user_id)
        permissions = [
            dto.Permission(PermissionType.UPDATE, allowed=True),
            dto.Permission(PermissionType.DELETE, allowed=True),
        ]

        try:
            memory_id = self._uow.memories_repo.create_memory(memory)
            self._permissions_gateway.add_for_memories(user_id, memory_id, permissions)
            self._uow.commit()
        except ApplicationException as exc:
            self._uow.rollback()
            raise exc

        return memory_id
