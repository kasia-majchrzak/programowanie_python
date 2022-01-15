from datetime import datetime

from modules.Osoba import Osoba


class Dietetyk(Osoba):
    @property
    def data_zatrudnienia(self) -> datetime:
        return self._data_zatrudnienia

    @data_zatrudnienia.setter
    def data_zatrudnienia(self, value: datetime):
        self._data_zatrudnienia = value

    def __init__(self, id: int, imie: str, nazwisko: str,
                 data_urodzenia: str, data_zatrudnienia: datetime):
        super().__init__(id, imie, nazwisko, data_urodzenia)
        self._data_zatrudnienia = data_zatrudnienia

    def __str__(self):
        return f'Dietetyk {self.imie} {self.nazwisko} - ' \
               f'data zatrudnienia: {self.data_zatrudnienia}'
