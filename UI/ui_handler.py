from abc import ABC, abstractmethod


class UIHandler(ABC):

    @abstractmethod
    def run(self):
        pass
