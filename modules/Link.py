class Link:
    @property
    def movieId(self) -> int:
        return self._movieId

    @movieId.setter
    def movieId(self, value: int):
        self._movieId = value

    @property
    def imdbId(self) -> str:
        return self._imdbId

    @imdbId.setter
    def imdbId(self, value: str):
        self._imdbId = value

    @property
    def tmdbId(self) -> str:
        return self._tmdbId

    @tmdbId.setter
    def tmdbId(self, value: str):
        self._tmdbId = value

    def __init__(self, movieId: int, imdbId: str, tmdbId: str):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId

    def __str__(self):
        return f'MovieId: {self.movieId}, imdbId: {self.imdbId}, tmdbId: {self.tmdbId}'
