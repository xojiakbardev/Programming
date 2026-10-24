import random
from abc import ABC, abstractmethod


class IConnection(ABC):
    @abstractmethod
    def get_session(self):
        pass


class DBConnect(IConnection):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__session = random.randint(0, 10)

        return cls.__instance

    def get_session(self):
        return self.__session


connection1 = DBConnect()
connection2 = DBConnect()
connection3 = DBConnect()
connection4 = DBConnect()
connection5 = DBConnect()

print(connection1.get_session())
print(connection2.get_session())
print(connection3.get_session())
print(connection4.get_session())
print(connection5.get_session())

print(connection1 is connection2 is connection3 is connection4 is connection5)
