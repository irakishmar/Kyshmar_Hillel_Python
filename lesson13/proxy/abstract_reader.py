from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def read(self):
        pass

class Writer(ABC):
    @abstractmethod
    def write(self, text):
        pass