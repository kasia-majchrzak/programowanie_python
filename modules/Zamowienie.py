from datetime import datetime

from modules.Dietetyk import Dietetyk
from modules.Pacjent import Pacjent


class Zamowienie:
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def pacjent(self) -> Pacjent:
        return self._pacjent

    @pacjent.setter
    def pacjent(self, value: Pacjent):
        self._pacjent = value

    @property
    def dietetyk(self) -> Dietetyk:
        return self._dietetyk

    @dietetyk.setter
    def dietetyk(self, value):
        self._dietetyk = value

    @property
    def diety(self) -> list:
        return self._diety

    @diety.setter
    def diety(self, value: list):
        self._diety = value

    @property
    def data_zamowienia(self) -> datetime:
        return self._data_zamowienia

    @data_zamowienia.setter
    def data_zamowienia(self, value):
        self._data_zamowienia = value

    def oblicz_wartosc(self) -> float:
        wartosc = 0
        for dieta in self.diety:
            wartosc += dieta.cena_za_dzien * dieta.ilosc_dni

        return wartosc.__round__(2)

    def oblicz_kalorycznosc(self) -> float:
        kalorycznosc = 0
        for dieta in self.diety:
            kalorycznosc += dieta.kalorycznosc_per_dzien

        return kalorycznosc.__round__(2)

    def __str__(self):
        return f'Zamówienie pacjenta ' \
               f'{self.pacjent.imie} {self.pacjent.nazwisko} ' \
               f'od dietetyka ' \
               f'{self.dietetyk.imie} {self.dietetyk.nazwisko}. ' \
               f'Łączna kaloryczność: {self.oblicz_kalorycznosc()}, ' \
               f'wartość: {self.oblicz_wartosc()}'
