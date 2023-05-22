def sum_of_parameters(*args):
    summa = 0
    for parameter in args:
        summa += parameter
    print(summa)


if __name__ == "__main__":
    sum_of_parameters(2, 2, 4, 8, 0)
