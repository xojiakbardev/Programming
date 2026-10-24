class Computer():
    def __init__(self):
        self._ram = None
        self._gpu = None
        self._cpu = None
        self._storage = None

    def setRam(self,ram:int):
        self._ram = ram
        return self

    def setGpu(self,gpu:int):
        self._gpu = gpu
        return self

    def setCpu(self,cpu:int):
        self._cpu = cpu
        return self

    def setStorage(self,storage:str):
        self._storage = storage
        return self

    def __str__(self):
        return (
            f"Copmuter: "
            f"\n ram: {self._ram}gb"
            f"\n cpu: {self._cpu}"
            f"\n gpu: {self._gpu}"
            f"\n storage: {self._storage}gb"
        )

computer = Computer().setRam(8).setCpu(4).setGpu(8).setStorage(250)

print(computer)
