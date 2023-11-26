class ApplicationException(Exception):
    @property
    def message(self) -> str:
        return "base application error message"

    @property
    def exception_type(self) -> str:
        return self.__class__.__name__
