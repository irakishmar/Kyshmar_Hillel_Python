def remove_numbers(text: str):
    for element in text:
        if element.isnumeric():
            text = text.replace(element, '')
    return text


if __name__ == "__main__":
    with open('your_file.txt', 'r') as file:
        text_str = file.read()
    with open('your_file.txt', 'w') as new_file:
        new_file.write(remove_numbers(text_str))
