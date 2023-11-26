from memories.applications.common.interfaces import UnitOfWork
from memories.applications.user.interfaces import user_repo


class UserUnitOfWork(UnitOfWork):
    user_repo: user_repo.UserRepo
