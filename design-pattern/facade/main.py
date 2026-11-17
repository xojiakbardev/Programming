class FlightBooking:

    def book(self, city: str):
        print(f"{city} ga aviachipta bron qilindi")

    def cancel(self, city: str):
        print(f"{city} ga aviachipta bekor qilindi")


class HotelBooking:

    def book(self, hotel: str):
        print(f"{hotel} mehmonxonasidan xona bron qilindi")

    def cancel(self, hotel: str):
        print(f"{hotel} mehmonxonasidagi bron bekor qilindi")


class Payment:

    def pay(self, amount: float):
        print(f"{amount} so'm to'lov amalga oshirildi")

    def refund(self, amount: float):
        print(f"{amount} so'm to'lov qaytarildi")


class TravelFacade:
    def __init__(self):
        self.flight = FlightBooking()
        self.hotel = HotelBooking()
        self.payment = Payment()

    def book_trip(self, city: str, hotel: str, amount: float):
        print("Sayohat bron qilinmoqda ...")
        self.flight.book(city)
        self.hotel.book(hotel)
        self.payment.pay(amount)
        print("Sayohat bron qilindi")
        print()

    def cancel_trip(self, city: str, hotel: str, amount: float):
        print("Sayohat bekor qilinmoqda ...")
        self.flight.cancel(city)
        self.hotel.cancel(hotel)
        self.payment.refund(amount)
        print("Sayohat bekor qilindi")
        print()


if __name__ == "__main__":
    travel = TravelFacade()
    travel.book_trip("Istanbul", "Hilton", 5000000)
    travel.cancel_trip("Istanbul", "Hilton", 5000000)
