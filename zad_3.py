def check_number(number: int) -> bool:
    return number % 2 == 0


print('Podaj liczbę:')
number_to_check = int(input())
result = check_number(number_to_check)

if result:
    print('Liczba parzysta')
else:
    print('Liczba nieparzysta')