def say_hello(name: str, surname: str) -> str:
    return f'Cześć {name} {surname}!'


print('Podaj imię: ')
name = input()
print('Podaj nazwisko:')
surname = input()
result = say_hello(name, surname)
print(result)
