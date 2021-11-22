from datetime import datetime

from zad_1 import Student


class Library:
    city: str
    street: str
    zip_code: str
    open_hours: str
    phone: str

    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Library in {self.city} ({self.zip_code})'


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


class Employee:
    first_name: str
    last_name: str
    hire_date: datetime
    birth_date: datetime
    city: str
    street: str
    zip_code: str
    phone: str

    def __init__(self, first_name: str, last_name: str, hire_date: datetime, birth_date: datetime, city: str,
                 street: str, zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'{self.first_name} {self.last_name} (hire date: {self.hire_date})'


class Order:
    employee: Employee
    student: Student
    books: list[Book]
    order_date: datetime

    def __init__(self, employee: Employee, student: Student, books: list[Book], order_date: datetime):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Student {self.student.name} borrowed {len(self.books)} books on {datetime.strftime(self.order_date, "%d.%m.%y")}'


libraryInKatowice = Library('Katowice', 'Warszawska 5', '40-000', '07:00-20:00', '682 283 283')
libraryInWarsaw = Library('Warszawa', 'Kościuszki 20', '00-200', '08:00-18:00', '849 738 829')

mrMercedesKing = Book(libraryInKatowice, datetime(2014, 6, 3), 'Stephen', 'King', 'Mr. Mercedes', 436)
findersKeepersKing = Book(libraryInKatowice, datetime(2015, 6, 2), 'Stephen', 'King', 'Finders Keepers', 480)
endOfWatchKing = Book(libraryInKatowice, datetime(2019, 9, 18), 'Stephen', 'King', 'End Of Watch', 442)
itKing = Book(libraryInWarsaw, datetime(1986, 9, 15), 'Stephen', 'King', 'It', 138)
dumaKeyKing = Book(libraryInWarsaw, datetime(2008, 9, 18), 'Stephen', 'King', 'Duma Key', 640)

firstEmployee = Employee('Adam', 'Nowak', datetime(2010, 3, 1), datetime(1960, 9, 20), 'Katowice'
                         , 'Opolska 15', '40-000', '748 837 728')
secondEmployee = Employee('Aleksandra', 'Kowalczyk', datetime(2014, 8, 1), datetime(1970, 8, 28), 'Katowice'
                          , 'Warszawska 28', '40-000', '738 291 339')
thirdEmployee = Employee('Zofia', 'Lewandowska', datetime(2005, 7, 10), datetime(1965, 4, 23), 'Warszawa'
                         , 'Kościuszki 110', '00-200', '838 283 292')

firstStudent = Student('Jan Kowalski', 40)
secondStudent = Student('Anna Kowalska', 80)
thirdStudent = Student('Piotr Nowak', 98)

firstOrder = Order(firstEmployee, secondStudent, [mrMercedesKing, findersKeepersKing], datetime.now())
secondOrder = Order(thirdEmployee, thirdStudent, [itKing, dumaKeyKing], datetime.now())

print(firstOrder)
print(secondOrder)
