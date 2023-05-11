# conditions
first_num = 2
second_num = 2

#arithmetic multiplication

first_multiplication = first_num * 2
second_multiplication = 2 * 2
third_multiplication = first_num * second_num
first_num *= 2
print('Four options for multiplying 2 numbers:')
print(f'1. first_num * 2 = {first_multiplication}', f'2. 2 * 2 = {second_multiplication}',
      f'3. first_num * second_num = {third_multiplication}', f'4. first_num *= {first_num}', sep = '\n')
print()

# bin operator (multiplication)
print('Result of binary AND operation')
fourth_multiplication = 2 & 2
print(f'2 & 2 = {bin(fourth_multiplication)}')
print()

print('Binary multiplication of two numbers:')
fifth_multiplication = 2 * 2
print(f'2 * 2 = {bin(fifth_multiplication)}')
print()

# conditions
first_num = 2
second_num = 2

#arithmetic float dividing
print('Three options for dividing 2 float numbers:')
first_float_dividing = first_num / 2
second_float_dividing = 2 / 2
third_float_dividing = first_num / second_num
first_num /= second_num
print(f'1. first_num / 2 = {first_float_dividing}', f'2. 2 / 2 = {second_float_dividing}',
      f'3. first_num / second_num = {third_float_dividing}', f'first_num /= {first_num}', sep='\n')
print()

# conditions
first_num = 2
second_num = 2

#arithmetic integer dividing
print('Three options for dividing 2 integer numbers:')
first_integer_dividing = first_num // 2
second_integer_dividing = 2 // 2
third_integer_dividing = first_num // second_num
second_num //= 2
print(f'1. first_num // 2 = {first_integer_dividing}', f'2. 2 // 2 = {second_integer_dividing}',
      f'3. first_num // second_num = {third_integer_dividing}', f'second_num //= {second_num}',  sep='\n')
print()

print('Binary dividing of two numbers:')
binary_dividing = 2 // 2
print(f'2 // 2 = {bin(binary_dividing)}')


