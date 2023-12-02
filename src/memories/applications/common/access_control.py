from memories.applications.common.exceptions import AccessDenied


class AccessControl:
    def can_update(self, current_user_id: int, owner_id: int) -> None:
        if current_user_id == owner_id:
            return
        raise AccessDenied()

    def can_delete(self, current_user_id: int, owner_id: int) -> None:
        if current_user_id == owner_id:
            return
        raise AccessDenied()
