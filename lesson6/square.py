import math


def square(square_side: int or float):
    perimeter = 4 * square_side
    area = square_side ** 2
    diagonal = square_side * (math.sqrt(2))
    return (perimeter, area, diagonal)


if __name__ == "__main__":
    print(square(4))
