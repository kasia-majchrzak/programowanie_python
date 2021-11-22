class Student:
    name: str
    marks: float

    def __init__(self, name: str, marks: float):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Student {self.name} (marks: {self.marks}) passed' if self.is_passed() \
            else f'Student {self.name} (marks: {self.marks}) not passed'

    def is_passed(self) -> bool:
        return self.marks > 50


firstStudent: Student = Student('Kowalski', 40)
secondStudent: Student = Student('Kowalska', 80)


print(firstStudent)
print(secondStudent)
