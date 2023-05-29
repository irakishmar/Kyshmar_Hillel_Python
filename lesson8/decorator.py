def print_function_name(func):
    def wrapper(*args):
        result = func(*args)
        print(f'Name of function is "{func.__name__}"')
        return result

    return wrapper


@print_function_name
def summa(*args):
    return sum(args)


@print_function_name
def multiplaction(*args):
    result = 1
    for num in args:
        result *= num
    return result


if __name__ == "__main__":
    print(f'Result:{summa(2, 3, 2)}')
    print(f'Result:{multiplaction(4, 5, 2)}')
