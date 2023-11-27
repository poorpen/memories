from memories.applications.common.interfaces import IdentityProvider, PermissionsGateway
from memories.applications.common.access_control import AccessControl
from memories.applications.common.exceptions import ApplicationException

from memories.domain.memory import value_objects
from memories.applications.memory.interfaces import MemoryUnitOfWork
from memories.applications.memory.models import command


class UpdateMemoryText:
    def __init__(
        self,
        identity_provider: IdentityProvider,
        permission_gateway: PermissionsGateway,
        uow: MemoryUnitOfWork,
    ):
        self._identity_provider = identity_provider
        self._permissions_gateway = permission_gateway
        self._access_control = AccessControl()
        self._uow = uow

    def __call__(self, command_data: command.UpdateText) -> None:
        user_id = self._identity_provider.identify()
        user_permissions = self._permissions_gateway.get_for_memory(
            user_id, command_data.memory_id
        )
        self._access_control.can_update(user_permissions)

        new_title = value_objects.text_block.Title(command_data.title)
        new_text = value_objects.text_block.Text(command_data.text)

        memory = self._uow.memory_repo.get_memory(command_data.memory_id)
        memory.update_text_block(new_title, new_text)

        try:
            self._uow.memory_repo.update_memory(memory)
            self._uow.commit()
        except ApplicationException as exc:
            self._uow.rollback()
            raise exc
