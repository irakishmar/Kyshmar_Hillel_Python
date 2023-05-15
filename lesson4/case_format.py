import re

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

# # for each word in camel list find matching regex and replace with _ and change to lower case
# for camel_word in camel_case:
#     snake_case.append(re.sub('([a-z])([A-Z])', r'\1_\2', camel_word).lower())

print(snake_case)
