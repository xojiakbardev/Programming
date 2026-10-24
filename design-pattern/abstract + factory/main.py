import abc

class Drink(abc.ABC):
    
    @abc.abstractmethod
    def prepare(self):
        pass




class Latte(Drink):
    def prepare(self):
        return "Latte tayyorlanmoqda"



class Tea(Drink):
    def prepare(self):
        return "Choy tayyorlanmoqda"





class DrinkFactory:
    def builder(self, drink_type):
        match drink_type:
            case "latte":
                return Latte()
            case "tea":
                return Tea()
            case _:
                raise ValueError(f"{drink_type} bunday tur yo")



class Cafe:
    def __init__(self, drink_factory: DrinkFactory):
        self.drink_factory = drink_factory

    def order(self, drink_type: str):
        drink = self.drink_factory.builder(drink_type)
        return drink.prepare()


if __name__ == "__main__":
    cafe = Cafe(
        drink_factory=DrinkFactory()
    )

    print(cafe.order("latte"))
    print(cafe.order("tea"))

