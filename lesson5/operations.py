with open('file_with_num', 'r') as file:
    numbers = file.readlines()
    for line in numbers:
        new_line = line.rstrip()
        list_with_num = new_line.split(' ')
        if list_with_num[2] == '1':
            operator = '+'
            result = int(list_with_num[0]) + int(list_with_num[1])
        elif list_with_num[2] == '2':
            operator = '-'
            result = int(list_with_num[0]) - int(list_with_num[1])
        else:
            operator = '*'
            result = int(list_with_num[0]) * int(list_with_num[1])

        print(list_with_num[0], operator, list_with_num[1], '=', result)
