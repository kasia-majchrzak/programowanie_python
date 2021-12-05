from datetime import datetime

from zad_1.modules.Student import Student
from zad_2.modules.Employee import Employee


class Order:
    employee: Employee
    student: Student
    books: list
    order_date: datetime

    def __init__(self, employee: Employee, student: Student, books: list, order_date: datetime):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Student {self.student.name} borrowed {len(self.books)} books on {datetime.strftime(self.order_date, "%d.%m.%y")}'