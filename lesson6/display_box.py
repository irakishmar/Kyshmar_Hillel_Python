def display_box(width: int, height: int, character: str):
    for i in range(1, height + 1):
        if i == 1 or i == height:
            print(character * width)
        else:
            print(character + ' ' * (width - 2) + character)


if __name__ == "__main__":
    display_box(5, 5, '*')
