from memories.applications.common.exceptions import ApplicationException


class UserAlreadyExist(ApplicationException):
    @property
    def message(self) -> str:
        return ""

