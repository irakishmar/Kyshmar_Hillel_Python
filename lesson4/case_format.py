camel_case = ["FirstItem", "FriendsList", "MyTuple"]
snake_case = list()
for part in camel_case:
    for symbol in (part[1:]):
        if symbol.isupper():
            index = part.index(symbol)
            new_case = part[:index] + "_" + part[index:]
            new_case = new_case.lower()
            snake_case.append(new_case)
            break
print(snake_case)