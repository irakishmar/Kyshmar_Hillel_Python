
from txt_reader import TxtReader
from txt_writer import TxtWriter
class TxtProxyWriterReader:
    def __init__(self, file_path):
        self.__txt_reader = TxtReader(file_path)
        self.__writer = TxtWriter(file_path)

    def read_file(self):

        return self.__txt_reader.read()

    def write_file(self, text):
        self.__writer.write(text)



if __name__ == '__main__':
    proxy_reader = TxtProxyWriterReader('data.txt')

    print(proxy_reader.read_file())
    print('*' * 10)
    proxy_reader.write_file("\nHello, World!")

    print(proxy_reader.read_file())