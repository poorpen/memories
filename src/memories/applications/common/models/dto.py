from dataclasses import dataclass

from memories.applications.common.constants import PermissionType


@dataclass
class Permission:
    type: PermissionType
    allowed: bool
