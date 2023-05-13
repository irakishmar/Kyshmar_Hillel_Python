import re

info_str = ' name=Amanda=sssss&age=32&&salary=1500&currency=euro '
info_str = info_str.strip()
info_str = info_str.replace('=sssss','')
dictionary = {}

info_str = list(filter(None, info_str.split('&')))

# # Regular expression (please comment out the previous line info_sting and check the additional task)
# info_str = list(filter(None, re.split("\&", info_str)))

for element in (info_str):
    key, value = element.split("=")
    dictionary[key] = value
print(dictionary)



