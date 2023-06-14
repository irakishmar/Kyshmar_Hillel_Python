from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, count_wheels: int, count_of_doors: int, count_of_windows: int, engine_type: str):
        self._count_wheels = count_wheels
        self._count_of_doors = count_of_doors
        self._count_of_windows = count_of_windows
        self._engine_type = engine_type

    @abstractmethod
    def move(self):
        pass
