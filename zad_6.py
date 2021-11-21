def create_new_list(first_list: list, second_list: list) -> list:
    return [number ** 3 for number in set(first_list + second_list)]