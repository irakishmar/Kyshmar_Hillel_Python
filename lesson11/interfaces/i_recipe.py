from abc import ABC, abstractmethod


class IRecipe(ABC):
    @abstractmethod
    def take_ingredients(self, milk: int, meal: int, egg: int, strawberry: int):
        pass

    @abstractmethod
    def mix_ingredients(self):
        pass

    @abstractmethod
    def move_to_baking_dish(self):
        pass
