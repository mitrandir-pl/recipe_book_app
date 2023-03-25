from abc import ABC, abstractmethod


class DatabaseHandler(ABC):

    @abstractmethod
    def connect(self, uri: str, user: str, password: str) -> None:
        pass

    @abstractmethod
    def close(self):
        pass
