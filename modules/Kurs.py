from datetime import datetime

from modules.FirmaSpozywcza import FirmaSpozywcza
from modules.Pojazd import Pojazd


class Kurs:
    @property
    def kierowca(self) -> str:
        return self._kierowca

    @kierowca.setter
    def kierowca(self, value):
        self._kierowca = value

    @property
    def adres_odbioru(self) -> str:
        return self._adres_odbioru

    @adres_odbioru.setter
    def adres_odbioru(self, value):
        self._adres_odbioru = value

    @property
    def adres_docelowy(self) -> str:
        return self._adres_docelowy

    @adres_docelowy.setter
    def adres_docelowy(self, value):
        self._adres_docelowy = value

    @property
    def data_wyjazdu(self) -> datetime:
        return self._data_wyjazdu

    @data_wyjazdu.setter
    def data_wyjazdu(self, value):
        self._data_wyjazdu = value

    @property
    def data_przyjazdu(self) -> datetime:
        return self._data_przyjazdu

    @data_przyjazdu.setter
    def data_przyjazdu(self, value):
        self._data_przyjazdu = value

    @property
    def pojazd(self) -> Pojazd:
        return self._pojazd

    @pojazd.setter
    def pojazd(self, value):
        self._pojazd = value

    @property
    def firma_spozywcza(self) -> FirmaSpozywcza:
        return self._firma_spozywcza

    @firma_spozywcza.setter
    def firma_spozywcza(self, value):
        self._firma_spozywcza = value

    @property
    def zaladunek_kg(self) -> float:
        return self._zaladunek_kg

    @zaladunek_kg.setter
    def zaladunek_kg(self, value):
        self._zaladunek_kg = value

    @property
    def odcinki(self) -> list:
        return self._odcinki

    @odcinki.setter
    def odcinki(self, value):
        self._odcinki = value

    def __init__(self, kierowca: str, adres_odbioru: str, adres_docelowy: str, data_wyjazdu: datetime,
                 data_przyjazdu: datetime, pojazd: Pojazd, firma_spozywcza: FirmaSpozywcza,
                 odcinki: list, zaladunek_kg: float):
        self.kierowca = kierowca
        self.adres_odbioru = adres_odbioru
        self.adres_docelowy = adres_docelowy
        self.data_wyjazdu = data_wyjazdu
        self.data_przyjazdu = data_przyjazdu
        self.pojazd = pojazd
        self.firma_spozywcza = firma_spozywcza
        self.odcinki = odcinki
        self.zaladunek_kg = zaladunek_kg

    def policz_sume_kilometrow(self):
        suma_kilometrow: float = 0.0

        for odcinek in self.odcinki:
            suma_kilometrow += odcinek.dlugosc

        return round(suma_kilometrow, 2)

    def zwroc_marke_pojazdu(self):
        return self.pojazd.marka

    def __str__(self):
        return f'Kurs wykonany od {self.data_wyjazdu} do {self.data_przyjazdu} przez kierowcę {self.kierowca} ' \
               f'pojazdem marki {self.zwroc_marke_pojazdu()} dla klienta {self.firma_spozywcza.nazwa}. ' \
               f'Łączna ilość kilometrów: {self.policz_sume_kilometrow()}, załadunek: {self.zaladunek_kg} kg'