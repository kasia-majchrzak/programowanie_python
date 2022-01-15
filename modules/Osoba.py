from datetime import datetime


class Osoba:
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def imie(self) -> str:
        return self._imie

    @imie.setter
    def imie(self, value: str):
        self._imie = value

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, value: str):
        self._nazwisko = value

    @property
    def data_urodzenia(self) -> datetime:
        return self._data_urodzenia

    @data_urodzenia.setter
    def data_urodzenia(self, value: datetime):
        self._data_urodzenia = value

    def __init__(self, id: int, imie: str, nazwisko: str,
                 data_urodzenia: datetime):
        self._id = id
        self._imie = imie
        self._nazwisko = nazwisko
        self._data_urodzenia = data_urodzenia

    def __str__(self):
        return f'{self.imie} {self.nazwisko} - ur. {self.data_urodzenia}'
