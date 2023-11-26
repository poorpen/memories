from typing import List

from memories.applications.common.exceptions import AccessDenied
from memories.applications.common.constants import PermissionType
from memories.applications.common.models.dto import Permission


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
