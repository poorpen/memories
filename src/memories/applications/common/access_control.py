from typing import List

from memories.applications.common.exceptions import ApplicationException
from memories.applications.common.constants import PermissionType
from memories.applications.common.models.dto import Permission


class AccessDenied(ApplicationException):
    @property
    def message(self) -> str:
        return "You do not have sufficient rights to perform this action"


class AccessControl:
    def can_update(self, user_permissions: List[Permission]) -> None:
        for permission in user_permissions:
            if permission.type == PermissionType.UPDATE and permission.allowed:
                return
        raise AccessDenied()

    def can_delete(self, user_permissions: List[Permission]) -> None:
        for permission in user_permissions:
            if permission.type == PermissionType.DELETE and permission.allowed:
                return
        raise AccessDenied()
