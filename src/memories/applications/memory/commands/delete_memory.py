from memories.applications.common.interfaces import IdentityProvider
from memories.applications.common.access_control import AccessControl
from memories.applications.common.exceptions import ApplicationException

from memories.applications.memory.interfaces import MemoryUnitOfWork
from memories.applications.memory.models import command


class DeleteMemory:
    def __init__(
        self,
        identity_provider: IdentityProvider,
        uow: MemoryUnitOfWork,
    ):
        self._identity_provider = identity_provider
        self._access_control = AccessControl()
        self._uow = uow

    def __call__(self, command_data: command.DeleteMemory) -> None:
        user_id = self._identity_provider.identify()
        memory = self._uow.memory_repo.get_memory(command_data.memory_id)

        self._access_control.can_delete(user_id, memory.owner_id)

        memory.delete()

        try:
            self._uow.memory_repo.update_memory(memory)
            self._uow.commit()
        except ApplicationException as exc:
            self._uow.rollback()
            raise exc
