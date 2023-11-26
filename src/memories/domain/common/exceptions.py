class DomainException(Exception):
    @property
    def message(self) -> str:
        return "base domain error message"

    @property
    def exception_type(self) -> str:
        return self.__class__.__name__