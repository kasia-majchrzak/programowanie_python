from datetime import datetime


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
