from datetime import datetime

from zad_2.modules.Library import Library


class Book:
    library: Library
    publication_date: datetime
    author_name: str
    author_surname: str
    title: str
    number_of_pages: int

    def __init__(self, library: Library, publication_date: datetime, author_name: str, author_surname: str,
                 title: str, number_of_pages: int):
        self.title = title
        self.number_of_pages = number_of_pages
        self.author_name = author_name
        self.author_surname = author_surname
        self.publication_date = publication_date
        self.library = library

    def __str__(self):
        return f'/"{self.title}/" written by {self.author_name} {self.author_surname} ({self.publication_date})'
