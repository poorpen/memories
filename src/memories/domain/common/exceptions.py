class AppException(Exception):
    @property
    def message(self) -> str:
        return "base app error message"

    @property
    def exception_type(self) -> str:
        return self.__class__.__name__


class DomainException(AppException):
    @property
    def message(self) -> str:
        return "some domain error message"
