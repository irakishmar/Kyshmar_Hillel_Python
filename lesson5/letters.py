
with open('text_for_letters.txt', 'r') as file:
    text = file.read()

letter_count = {}

for symbol in text:
    if symbol.isalpha():
        symbol = symbol.lower()
        if symbol in letter_count:
            letter_count[symbol] += 1
        else:
            letter_count[symbol] = 1

for letter, count in letter_count.items():
    print(f"The letter'{letter}' occurs in the text {count} times")
