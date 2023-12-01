from memories.domain.common.exceptions import AppException


class ApplicationException(AppException):
    @property
    def message(self) -> str:
        return "base application error message"


class AccessDenied(ApplicationException):
    @property
    def message(self) -> str:
        return "You do not have sufficient rights to perform this action"


class AuthError(ApplicationException):
    @property
    def message(self) -> str:
        return "User with this password and email address does not exist"


class UnexpectedAppError(ApplicationException):
    @property
    def message(self) -> str:
        return "Unexpected error"


class RepoError(UnexpectedAppError):
    @property
    def message(self) -> str:
        return "Unexpected repository error"
