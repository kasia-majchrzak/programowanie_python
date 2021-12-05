class Odcinek:
    @property
    def miejsce_poczatkowe(self) -> str:
        return self._miejsce_poczatkowe

    @miejsce_poczatkowe.setter
    def miejsce_poczatkowe(self, value):
        self._miejsce_poczatkowe = value

    @property
    def miejsce_koncowe(self) -> str:
        return self._miejsce_koncowe

    @miejsce_koncowe.setter
    def miejsce_koncowe(self, value):
        self._miejsce_koncowe = value

    @property
    def dlugosc(self) -> float:
        return self._dlugosc

    @dlugosc.setter
    def dlugosc(self, value):
        self._dlugosc = value

    @property
    def koszt_za_kilometr(self) -> float:
        return self._koszt_za_kilometr

    @koszt_za_kilometr.setter
    def koszt_za_kilometr(self, value):
        self._koszt_za_kilometr = value

    @property
    def koszt(self) -> float:
        return self._koszt

    @koszt.setter
    def koszt(self, value):
        self._koszt = value

    def __init__(self, miejsce_poczatkowe: str, miejsce_koncowe: str, dlugosc: float, koszt_za_kilometr: float):
        self.miejsce_poczatkowe = miejsce_poczatkowe
        self.miejsce_koncowe = miejsce_koncowe
        self.dlugosc = dlugosc
        self.koszt_za_kilometr = koszt_za_kilometr
        self.koszt = dlugosc * koszt_za_kilometr

    def __str__(self):
        return f'Odcinek {self.miejsce_poczatkowe} - {self.miejsce_koncowe}. Długość {self.dlugosc}km, koszt {self.koszt}zł'