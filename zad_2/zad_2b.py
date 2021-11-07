def print_list(elements: list()):
    for element in elements:
        print(element)


def multiply_numbers_using_for(numbers: list()):
    for idx, number in enumerate(numbers):
        numbers[idx] = number * 2

    return numbers


def multiply_numbers_using_list(numbers):
    return [number * 2 for number in numbers]


listOfNumbers: list() = [1, 2, 3, 4, 5]
print_list(multiply_numbers_using_for(listOfNumbers))
print_list(multiply_numbers_using_list(listOfNumbers))


