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
