from math import *
from typing import Callable, List


def map_fun(func: Callable[[int, float, str], int or str], iterable: List[int]) -> List[int]:
    list_number = []
    for element in iterable:
        list_number.append(func(element))
    return list_number


def exponentiation_fun(numbers: int, degree: int = 2) -> int:
    result = int(pow(numbers, degree))
    return result


def round_num(number: float) -> int:
    result = round(number)
    return result


def title_word(text: str) -> str:
    result = text.title()
    return result


int_numbers = [0, 2, 4, 6, 8, 10]
float_num = [1.11, 2.45, 0.46, 45.66]
degree_of_number = 2
lower_case = ['the', 'sun', 'also', 'rises']
if __name__ == "__main__":
    exponentiation_numbers = (list(map_fun(exponentiation_fun, int_numbers)))
    rounded_numbers = (list(map_fun(round_num, float_num)))
    title_text = (list(map_fun(title_word, lower_case)))
    print(f'Numbers to the power of 2: {exponentiation_numbers}')
    print(f'Rounded numbers: {rounded_numbers}')
    print(f'Title text: {title_text}')
