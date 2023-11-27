class ApplicationException(Exception):
    @property
    def message(self) -> str:
        return "base application error message"

    @property
    def exception_type(self) -> str:
        return self.__class__.__name__


class AccessDenied(ApplicationException):
    @property
    def message(self) -> str:
        return "You do not have sufficient rights to perform this action"


class AuthError(ApplicationException):
    @property
    def message(self) -> str:
        return "User with this password and email address does not exist"


class RepoError(ApplicationException):
    @property
    def message(self) -> str:
        return "Unexpected repository error"
