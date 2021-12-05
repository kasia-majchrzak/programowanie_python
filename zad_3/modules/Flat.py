from zad_3.modules.Property import Property


class Flat(Property):
    floor: int

    def __init__(self, area: str, rooms: int, price: float, address: str, floor: int):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
        self.floor = floor

    def __str__(self):
        return f'Flat in {self.area} on {self.address}: {self.rooms} rooms, {self.floor} floor, {self.price} zł'
