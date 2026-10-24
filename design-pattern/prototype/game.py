from abc import ABC, abstractmethod
import copy
from dataclasses import dataclass


class Copyable(ABC):
    @abstractmethod
    def clone(self):
        pass


@dataclass
class GameCharacter():
    __id: int
    __name: str
    __level: int
    __weapon: str

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, value):
        self.__name = value

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__name = value

    def deep_clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return (f"Character(id={self.id}, name={self.name}, weapon={self.weapon},level={self.level})")


@dataclass
class CharacterFactory():
    __character: GameCharacter

    def set_character(self, character:GameCharacter):
        self.__character=character

    def clone_character(self):
        return self.__character.deep_clone()


class GameRunner():
    @staticmethod
    def main():
        ruzimuhammad = GameCharacter(12,"Ro'zimuhammad",3,"pichoq")
        factory = CharacterFactory(ruzimuhammad)

        men = factory.clone_character()
        men.name = "Xojiakbar"

        print(ruzimuhammad is men)
        print(ruzimuhammad)
        print(men)

        factory.set_character(men)

        men2 = factory.clone_character()
        print(men2)



if __name__=="__main__":
    GameRunner.main()
