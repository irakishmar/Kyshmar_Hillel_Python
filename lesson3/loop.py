numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_index = []
even_index = []
for index, number in enumerate(numbers):
    if number % 2 == 1:
        odd_index.append((index, number))
    else:
        even_index.append((index, number))
print(f'List with odd numbers: {odd_index}')
print(f'List with even numbers: {even_index}')
