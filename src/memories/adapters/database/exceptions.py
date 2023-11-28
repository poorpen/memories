from memories.applications.common.exceptions import ApplicationException


class CommitError(ApplicationException):
    @property
    def message(self) -> str:
        return "An error occurred during the commit"


class RollbackError(ApplicationException):
    @property
    def message(self) -> str:
        return "An error occurred during the rollback"
