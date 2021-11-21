def multiply(first: int, second: int) -> int:
    return first * second


print('Podaj pierwszą liczbę:')
first_variable = int(input())
print('Podaj drugą liczbę:')
second_variable = int(input())

print(f'Wynik to {multiply(first_variable, second_variable)}')