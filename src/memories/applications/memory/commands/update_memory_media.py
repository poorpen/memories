from memories.applications.common.interfaces import IdentityProvider
from memories.applications.common.access_control import AccessControl
from memories.applications.common.exceptions import ApplicationException

from memories.domain.memory import value_objects
from memories.applications.memory.interfaces import MemoryUnitOfWork
from memories.applications.memory.models import command


class UpdateMemoryMedia:
    def __init__(
        self,
        identity_provider: IdentityProvider,
        uow: MemoryUnitOfWork,
    ):
        self._identity_provider = identity_provider
        self._access_control = AccessControl()
        self._uow = uow

    def __call__(self, command_data: command.UpdateMedia) -> None:
        user_id = self._identity_provider.identify()
        memory = self._uow.memory_repo.get_memory(command_data.memory_id)

        self._access_control.can_update(user_id, memory.owner_id)

        new_photo = value_objects.media.Photo(command_data.photo)

        memory.update_media(new_photo)

        try:
            self._uow.memory_repo.update_memory(memory)
            self._uow.commit()
        except ApplicationException as exc:
            self._uow.rollback()
            raise exc
