class Dieta:
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @nazwa.setter
    def nazwa(self, value: str):
        self._nazwa = value

    @property
    def opis(self) -> str:
        return self._opis

    @opis.setter
    def opis(self, value: str):
        self._opis = value

    @property
    def typ(self) -> str:
        return self._typ

    @typ.setter
    def typ(self, value: str):
        self._typ = value

    @property
    def liczba_posilkow(self) -> int:
        return self._liczba_posilkow

    @liczba_posilkow.setter
    def liczba_posilkow(self, value: int):
        self._liczba_posilkow = value

    @property
    def kalorycznosc_per_dzien(self) -> int:
        return self._kalorycznosc_per_dzien

    @kalorycznosc_per_dzien.setter
    def kalorycznosc_per_dzien(self, value: int):
        self._kalorycznosc_per_dzien = value

    @property
    def cena_za_dzien(self) -> float:
        return self._cena_za_dzien

    @cena_za_dzien.setter
    def cena_za_dzien(self, value: float):
        self._cena_za_dzien = value

    @property
    def ilosc_dni(self) -> int:
        return self._ilosc_dni

    @ilosc_dni.setter
    def ilosc_dni(self, value: int):
        self._ilosc_dni = value

    def __init__(self, id: int, nazwa: str, opis: str, typ: str,
                 liczba_posilkow: int, kalorycznosc_per_dzien: int,
                 ilosc_dni: int, cena_za_dzien: float):
        self._id = id
        self._nazwa = nazwa
        self._opis = opis
        self._typ = typ
        self._liczba_posilkow = liczba_posilkow
        self._kalorycznosc_per_dzien = kalorycznosc_per_dzien
        self._cena_za_dzien = cena_za_dzien
        self._ilosc_dni = ilosc_dni

    def __str__(self):
        return f'Dieta {self.nazwa}: typ - {self.typ}, ' \
               f'kaloryczność w ciągu dnia - {self.kalorycznosc_per_dzien}, ' \
               f'liczba posiłków - {self.liczba_posilkow}'
