
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List



class IFileSystem(ABC):

    @abstractmethod
    def read():
        pass



@dataclass
class File(IFileSystem):
    name: str

    def read(self):
        print(f"{self.name} File reading ...")



class Folder(IFileSystem):
    def __init__(self, name: str):
        self.name = name
        self.components:List[IFileSystem] = []

    def read(self):
        print(f"{self.name} Folder reading ...")
        for file in self.components:
            file.read()
        print()


    def add(self, comp:IFileSystem):
        self.components.append(comp)


if __name__ == "__main__":
    folder = Folder("My Projects")
    folder.add(File("system.txt"))
    folder.read()

    folder2 = Folder("LabbayAI")
    folder.add(folder2)
    folder.read()
    file4 = File("main.py")
