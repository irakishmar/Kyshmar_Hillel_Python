from typing import Union


def max_func(*args: Union[int, float]) -> Union[int, float]:
    if len(args) == 0:
        raise ValueError("No numbers to compare")
    else:
        max_num = args[0]
        for element in args:
            if element > max_num:
                max_num = element
    return max_num


def min_func(*args: Union[int, float]) -> Union[int, float]:
    if len(args) == 0:
        raise ValueError("No numbers to compare")
    else:
        min_num = args[0]
        for element in args:
            if element < min_num:
                min_num = element
    return min_num


numbers = [1, 2, 3, 44, 55, 6666, 7, 0.1, 400]
# numbers = []

if __name__ == "__main__":
    try:
        max_number = (max_func(*numbers))
        min_number = (min_func(*numbers))
        print(f'Maximum number from list is {max_number}')
        print(f'Minimum number from list is {min_number}')
    except ValueError as error:
        print(error)
