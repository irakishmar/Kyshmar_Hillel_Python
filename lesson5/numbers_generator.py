import random
import os

file_with_num = os.path.abspath('.')
list_with_tuple = []
tuple_with_num = tuple()
for num in range(0, 100):
    left_operand = str(random.randint(1, 100))
    right_operand = str(random.randint(1, 100))
    operator = str(random.randint(1, 3))
    tuple_with_num = (left_operand, right_operand, operator)
    list_with_tuple.append(tuple_with_num)

with open('file_with_num', 'a') as file:
    for element in list_with_tuple:
        element = ' '.join(element)
        file.write(str(element) + '\n')
