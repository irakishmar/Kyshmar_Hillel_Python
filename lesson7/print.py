import sys


def print_func(*args: str, sep: str, end: str, file=sys.stdout):
    text_list = []
    for item in args:
        text_list.append(item)
    output_text = sep.join(text_list) + end
    file.write(output_text)

if __name__ == "__main__":
    print_func('Implementation', 'of', 'my', 'own', 'print', 'function', sep=' ', end='\n', file=sys.stdout)
