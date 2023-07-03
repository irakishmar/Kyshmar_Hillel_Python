from abstract_reader import Writer

from abstract_reader import Writer
class TxtWriter(Writer):
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, text):
        with open(self.file_path, 'a') as file:
            file.write(text)