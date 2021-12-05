class Movie:
    @property
    def movieId(self) -> int:
        return self._movieId

    @movieId.setter
    def movieId(self, value: int):
        self._movieId = value

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value

    @property
    def genres(self) -> str:
        return self._genres

    @genres.setter
    def genres(self, value: str):
        self._genres = value

    def __init__(self, movieId: int, title: str, genres: str):
        self.movieId = movieId
        self.title = title
        self.genres = genres

    def __str__(self):
        return f'{self.title} (genre(-s): {self.genres})'
