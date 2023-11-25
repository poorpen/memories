from memories.domain.common.exceptions import DomainException

class MemeryIsDeleted(DomainException):

    @property
    def message(self) -> str:
        return "Memory is deleted"