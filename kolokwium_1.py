from datetime import datetime


class Firma:
    @property
    def nazwa(self) -> str:
        return self._nazwa

    @nazwa.setter
    def nazwa(self, value):
        self._nazwa = value

    @property
    def adres(self) -> str:
        return self._adres

    @adres.setter
    def adres(self, value):
        self._adres = value

    @property
    def nip(self) -> str:
        return self._nip

    @nip.setter
    def nip(self, value):
        self._nip = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def telefon(self) -> str:
        return self._telefon

    @telefon.setter
    def telefon(self, value):
        self._telefon = value

    def __init__(self, nazwa: str, adres: str, nip: str, email: str, telefon: str):
        self.nazwa = nazwa
        self.adres = adres
        self.nip = nip
        self.email = email
        self.telefon = telefon

    def __str__(self):
        return f'{self.nazwa} ({self.adres}): email {self.email}, tel. {self.telefon}, nip {self.nip}.'


class Pojazd:
    @property
    def marka(self) -> str:
        return self._marka

    @marka.setter
    def marka(self, value):
        self._marka = value

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def rok_produkcji(self) -> int:
        return self._rok_produkcji

    @rok_produkcji.setter
    def rok_produkcji(self, value):
        self._rok_produkcji = value

    @property
    def przebieg(self) -> float:
        return self._przebieg

    @przebieg.setter
    def przebieg(self, value):
        self._przebieg = value

    @property
    def moc_silnika(self) -> float:
        return self._moc_silnika

    @moc_silnika.setter
    def moc_silnika(self, value):
        self._moc_silnika = value

    @property
    def max_zaladunek_kg(self) -> float:
        return self._max_zaladunek_kg

    @max_zaladunek_kg.setter
    def max_zaladunek_kg(self, value):
        self._max_zaladunek_kg = value

    def __init__(self, marka: str, model: str, rok_produkcji: int, przebieg: float, moc_silnika: float
                 , max_zaladunek_kg: float):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg
        self.moc_silnika = moc_silnika
        self.max_zaladunek_kg = max_zaladunek_kg

    def __str__(self):
        return f'Pojazd {self.marka} {self.model} ({self.rok_produkcji})'


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


mercedes_vito = Pojazd('Mercedes-Benz', 'Vito', 2018, 210546.86, 150, 1000)
katowice_czestochowa = Odcinek('Katowice', 'Częstochowa', 88.565, 5)
czestochowa_lodz = Odcinek('Częstochowa', 'Łódź', 106.565, 5)
firma_spozywcza = FirmaSpozywcza('Food', 'Katowice, ul. Długa 5', '438320974', 'food@gmail.com', 678492747,
                                 datetime(2019, 11, 21, 8, 0, 0))
kurs = Kurs('Kowalski Jan', 'Katowice, ul. Długa 5', 'Łódź, ul. Kościuszki 54', datetime(2021, 11, 25, 6, 0, 0),
            datetime(2021, 11, 25, 11, 0, 0), mercedes_vito, firma_spozywcza, [katowice_czestochowa, czestochowa_lodz],
            800)

print(kurs)
