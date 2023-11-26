from typing import Protocol


from memories.domain.user.models import User


class UserRepo(Protocol):
    def add_user(self, user: User) -> None:
        raise NotImplemented
