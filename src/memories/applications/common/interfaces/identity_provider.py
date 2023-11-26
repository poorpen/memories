from typing import Protocol


class IdentityProvider(Protocol):
    def identify(self) -> int:
        raise NotImplemented
