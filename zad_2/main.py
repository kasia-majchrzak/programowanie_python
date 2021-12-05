from datetime import datetime

from zad_1.modules.Student import Student
from zad_2.modules.Library import Library
from zad_2.modules.Book import Book
from zad_2.modules.Employee import Employee
from zad_2.modules.Order import Order

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
