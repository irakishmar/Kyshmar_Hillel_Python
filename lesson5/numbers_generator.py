import random
import os

file_with_num = os.path.abspath('.')
tuple_with_num = ()
for num in range(0, 100):
    left_operand = str(random.randint(1, 100))
    right_operand = str(random.randint(1, 100))
    operator = str(random.randint(1, 3))
    tuple_with_num = (left_operand, right_operand, operator)
    my_str = ' '.join(tuple_with_num)
    with open('file_with_num', 'a') as file:
        file.write(my_str + '\n')
