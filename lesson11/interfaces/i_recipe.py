from abc import ABC, abstractmethod


class IRecipe(ABC):
    @abstractmethod
    def _take_ingredients(self, milk: int, meal: int, egg: int, strawberry: int):
        pass

    @abstractmethod
    def _mix_ingredients(self):
        pass

    @abstractmethod
    def _move_to_baking_dish(self):
        pass
