import datetime

from modules.Firma import Firma


class FirmaSpozywcza(Firma):
    @property
    def data_pierwszego_kursu(self) -> datetime:
        return self.data_pierwszego_kursu

    @data_pierwszego_kursu.setter
    def data_pierwszego_kursu(self, value):
        self._data_pierwszego_kursu = value

    def __init__(self, nazwa: str, adres: str, nip: str, email: str, telefon: str,
                 data_pierwszego_kursu: datetime):
        super().__init__(nazwa, adres, nip, email, telefon)
        self.data_pierwszego_kursu = data_pierwszego_kursu

    def __str__(self):
        return f'{super} Klient od {self.data_pierwszego_kursu}'