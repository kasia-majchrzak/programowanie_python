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