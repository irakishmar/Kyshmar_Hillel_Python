def squares_elements():
    for number in range(0, 1000000001, 2):
        yield number ** 2
