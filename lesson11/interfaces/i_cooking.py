from abc import ABC, abstractmethod


class ICooking(ABC):

    @abstractmethod
    def open_oven(self):
        pass

    @abstractmethod
    def put_in_the_oven(self):
        pass

    @abstractmethod
    def close_oven(self):
        pass

    @abstractmethod
    def waiting(self):
        pass

    @abstractmethod
    def turn_on_oven(self, oven_temperature: int):
        pass

    @abstractmethod
    def take_out_from_the_oven(self):
        pass

    @abstractmethod
    def turn_off_oven(self):
        pass
