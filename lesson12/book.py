class Book:
    def __init__(self, author, book_name, year):
        self.__author = author
        self.__book_name = book_name
        self.__year = year

    def __str__(self):
        result = f'{self.__class__.__name__}:\n{{\n \t author:{self.__author}\n \t book_name:{self.__book_name}\n \t ' \
                 f'year:{self.__year}\n}}'
        return result


if __name__ == '__main__':
    book = Book('Bernard Cornwell', 'Death of Kings', 2011)
    print(book)
