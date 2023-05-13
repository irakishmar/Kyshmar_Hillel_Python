import re

page = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My super star task</title>
</head>
<body>
    <div id="block-with-links">
        <div id="google">
            <a href="www.google.com">
                Google
            </a>
        <div/>
        <div id="facebook">
            <a href="http://facebook.com/dign-in">
                Facebook
            </a>
        </div>
            <div id="amazon">
                <a href="amazon.com">
                    Amazon
                </a>
            </div>
        </div>
    </div>
</body>
</html>'''

sentences_list = re.findall(r'\"[A-z]{3,}"|\"[A-z]{1,}?:?\/?\/?\.?[A-z]{1,}\.com\"|\"[A-z]{1,}:\/\/[A-z]{1,}.com\/[A-z]{1,}-[A-z]{1,}"|\n\s{1,}[A-z]{1,}', page)

# # additional task (please comment out the previous line sentences_list and check additional task)
# sentences_list = re.findall(r'\"[A-z]{3,}"|\w{1,}.com|\n\s{1,}[A-z]{1,}\n', page)

new_sentences = []
count = 1
google = list()
facebook = list()
amazon = list()
for item in sentences_list:
    item = item.strip()
    if '"' in item:
        item = item.replace('"', '')
        new_sentences.append(item)
    else:
        new_sentences.append(item)
for item in new_sentences:
    if count <=3:
        google.append(item)
        count +=1
    elif 3 < count <= 6:
        facebook.append(item)
        count +=1
    else:
        amazon.append(item)
print(tuple(google), tuple(facebook), tuple(amazon))