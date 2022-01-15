from modules.Osoba import Osoba


class Pacjent(Osoba):
    @property
    def alergeny(self) -> list:
        return self._alergeny

    @alergeny.setter
    def alergeny(self, value: list):
        self._alergeny = value

    def __init__(self, id: int, imie: str, nazwisko: str,
                 data_urodzenia: str, alergeny: list):
        super().__init__(id, imie, nazwisko, data_urodzenia)
        self._alergeny = alergeny

    def __str__(self):
        return f'Pacjent {self.imie} {self.nazwisko} - ' \
               f'alergeny: {str.join(", ", self.alergeny)}'
