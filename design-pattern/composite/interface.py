from abc import ABC, abstractmethod


class IFile(ABC):

    @abstractmethod
    def read()->str:
        pass
