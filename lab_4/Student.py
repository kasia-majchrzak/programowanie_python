class Student:
    name: str
    marks: float
    is_passed: bool


    def __init__(self, name: str, marks: float):
        self.name = name
        self.marks = marks
        self.is_passed = marks > 50


    def __str__(self):
        return f'Student {self.name} (mark: {self.marks}, passed: {self.is_passed})'
