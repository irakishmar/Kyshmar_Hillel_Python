from abc import ABC, abstractmethod


class ICooking(ABC):

    @abstractmethod
    def _open_oven(self):
        pass

    @abstractmethod
    def _put_in_the_oven(self):
        pass

    @abstractmethod
    def _close_oven(self):
        pass

    @abstractmethod
    def _waiting(self):
        pass

    @abstractmethod
    def _turn_on_oven(self, oven_temperature: int):
        pass

    @abstractmethod
    def _take_out_from_the_oven(self):
        pass

    @abstractmethod
    def _turn_off_oven(self):
        pass
