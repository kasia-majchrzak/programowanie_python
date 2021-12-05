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
