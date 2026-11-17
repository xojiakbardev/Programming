from abc import ABC, abstractmethod


class Order(ABC):

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass


class BasicOrder(Order):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_description(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price


class OrderDecorator(Order):
    def __init__(self, order: Order):
        self.order = order

    def get_description(self) -> str:
        return self.order.get_description()

    def get_price(self) -> float:
        return self.order.get_price()


class GiftWrapDecorator(OrderDecorator):

    def get_description(self) -> str:
        return self.order.get_description() + " + sovg'a qadoqlash"

    def get_price(self) -> float:
        return self.order.get_price() + 15000


class ExpressDeliveryDecorator(OrderDecorator):

    def get_description(self) -> str:
        return self.order.get_description() + " + tezkor yetkazib berish"

    def get_price(self) -> float:
        return self.order.get_price() + 30000


if __name__ == "__main__":
    order = BasicOrder("Kitob", 80000)
    print(order.get_description(), order.get_price())

    order = GiftWrapDecorator(order)
    print(order.get_description(), order.get_price())

    order = ExpressDeliveryDecorator(order)
    print(order.get_description(), order.get_price())
