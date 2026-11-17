from typing import List


class BlockType:
    def __init__(self, name: str, texture: str, color: str):
        self.name = name
        self.texture = texture
        self.color = color


class BlockFactory:
    data = {
        "Grass": ("img1.png", "green"),
        "Stone": ("img2.png", "gray"),
        "Dirt": ("img3.png", "brown"),
    }

    def __init__(self):
        self.types = {}

    def get_type(self, name: str) -> BlockType:
        if name not in self.types:
            texture, color = self.data[name]
            self.types[name] = BlockType(name, texture, color)
        return self.types[name]




class Block:
    def __init__(self, x: int, y: int, z: int, block_type: BlockType):
        self.x = x
        self.y = y
        self.z = z
        self.block_type = block_type

    def render(self):
        print(f"({self.x}, {self.y}, {self.z}) {self.block_type.name} {self.block_type.texture} {self.block_type.color}")

class World:
    def __init__(self):
        self.factory = BlockFactory()
        self.blocks:List[Block] = []

    def add_block(self, x: int, y: int, z: int, name: str):
        block_type = self.factory.get_type(name)
        self.blocks.append(Block(x, y, z, block_type))

    def render(self):
        for block in self.blocks:
            block.render()

if __name__ == "__main__":
    world = World()

    world.add_block(0, 0, 0, "Grass")
    world.add_block(1, 0, 0, "Grass")
    world.add_block(2, 0, 0, "Stone")
    world.add_block(3, 0, 0, "Grass")
    world.add_block(4, 0, 0, "Dirt")

    world.render()
    print()

    print(world.blocks[0].block_type is world.blocks[1].block_type)
    print(world.blocks[0].block_type is world.blocks[3].block_type)
    print(world.blocks[0].block_type is world.blocks[2].block_type)
