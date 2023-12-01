from memories.applications.common.interfaces import UnitOfWork
from memories.applications.user.interfaces.user_repo import UserRepo


class UserUnitOfWork(UnitOfWork):
    user_repo: UserRepo
