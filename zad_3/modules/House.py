from zad_3.modules.Property import Property


class House(Property):
    plot: int

    def __init__(self, area: str, rooms: int, price: float, address: str, plot: int):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
        self.plot = plot

    def __str__(self):
        return f'House in {self.area} on {self.address}: {self.rooms} rooms, plot: {self.plot} m2, {self.price} zł'
