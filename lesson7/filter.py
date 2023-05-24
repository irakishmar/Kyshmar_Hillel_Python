from typing import Callable, Union


def filter_func(condition: Callable[[Union[str, int]], int or float or str], iterable: Union[str, int, float]) -> list:
    filtered_elements = []
    for element in iterable:
        if condition(element):
            filtered_elements.append(element)
    return filtered_elements


def no_zero(element: int) -> int:
    if element != 0:
        return element


def is_even(element: int) -> int:
    if element != 0 and element % 2 == 0:
        return element


def no_empty(element: str) -> str:
    if element != ' ':
        return element


def graeter_than_zero(element: float) -> float:
    if element >= 1:
        return element


numbers = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0]
my_list = ['Liza', 'Sara', ' ', 'Tom', ' ']
float_num = [1.12, 0.56, 0.99, 4.54]

if __name__ == "__main__":
    no_zero_numbers = list(filter_func(no_zero, numbers))
    even_numbers = list(filter_func(is_even, numbers))
    no_empty_elements = list(filter_func(no_empty, my_list))
    number_greater_zero = list(filter_func(graeter_than_zero, float_num))
    print(f'List not containing zeros: {no_zero_numbers}')
    print(f'List containing even numbers: {even_numbers}')
    print(f'List with no empty elements: {no_empty_elements}')
    print(f'List with numbers greater than zero: {number_greater_zero}')
