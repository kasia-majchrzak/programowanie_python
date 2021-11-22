class Property:
    area: str
    rooms: int
    price: float
    address: str

    def __init__(self, area: str, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'Property in {self.area} on {self.address}: {self.rooms} rooms, {self.price} zł'


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


flatInWarsaw = Flat('Warszawa', 3, 500000, 'Kościuszki 40', 3)
houseInWarsaw = House('Warszawa', 8, 680000, 'Warszawska 7', 330)

print(flatInWarsaw)
print(houseInWarsaw)
