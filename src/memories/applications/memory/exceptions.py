from memories.applications.common.exceptions import ApplicationException


class MemoryNotExist(ApplicationException):
    @property
    def message(self) -> str:
        return "Memory with the specified id does not exist"
