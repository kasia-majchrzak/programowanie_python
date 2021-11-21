import datetime

from lab_4 import Student
from lab_4.lab_2 import Employee, Book


class Order:
    employee: Employee
    student: Student
    books: list[Book]
    order_date: datetime


    def __str__(self):
        return f'Student {self.student.name} borrowed: {str.join(self.books, ", ")}'
