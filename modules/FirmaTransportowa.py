from modules.Firma import Firma


class FirmaTransportowa(Firma):
    @property
    def ilosc_pojazdow(self) -> int:
        return self._ilosc_pojazdow

    @ilosc_pojazdow.setter
    def ilosc_pojazdow(self, value):
        self._ilosc_pojazdow = value

    def __init__(self, nazwa: str, adres: str, nip: str, email: str, telefon: str, ilosc_pojazdow: int):
        super().__init__(nazwa, adres, nip, email, telefon)
        self.ilosc_pojazdow = ilosc_pojazdow

    def __str__(self):
        return f'{super} Ilość pojazdów {self.ilosc_pojazdow}'