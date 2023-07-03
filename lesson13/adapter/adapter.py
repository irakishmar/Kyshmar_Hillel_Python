class FromTxtToJsonAdapter:
    def __init__(self, file_path):
        self.__file_path = file_path

    def txt_to_html(self):
        with open(self.__file_path, 'r') as file:
            lines = file.readlines()

        data = []
        headers = lines[0].replace('\n', '').split(',')
        for line in lines[1:]:
            line = line.split(',')
            data.append(dict(zip(headers,line)))


        html_doc = ''
        for item in data:
            for key, value in item.items():
                html_doc += f'<{key}>{value}</{key}>\n'
        return html_doc

if __name__ == '__main__':
    html_text = FromTxtToJsonAdapter('author.txt')
    print(html_text.txt_to_html())