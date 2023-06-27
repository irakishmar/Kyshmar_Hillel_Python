from interfaces.i_recipe import IRecipe
from interfaces.i_cooking import ICooking


# Inheritance
# Abstraction


class Pie(ICooking, IRecipe):
    def __init__(self, milk: int, meal: int, egg: int, strawberry: int, oven_temperature: int):
        # Hiding
        self.__is_open_oven = False
        self.__is_empty_oven = True
        self.__oven_temperature = oven_temperature
        self.__milk = milk
        self.__meal = meal
        self.__egg = egg
        self.__strawberry = strawberry
        self.__plate = []
        self.__baking_dish = ()

    # Polymorphism

    def _take_ingredients(self, milk: int, meal: int, egg: int, strawberry: int):
        if milk == 300 and meal == 400 and egg == 2:
            self.__plate = {
                "milk": milk,
                "meal": meal,
                "egg": egg,
                "strawberry": strawberry
            }
            print(
                f'Please take {self.__milk} ml of milk, {self.__meal} g of flour, {self.__egg} eggs and strawberries.')
        else:
            if milk != 300:
                print('You took the wrong amount of milk.')
            elif meal != 400:
                print('You took the wrong amount of meal.')
            elif egg != 2:
                print('You took the wrong amount of eggs.')

    def _mix_ingredients(self):
        print(f'Please mix {self.__plate}')

    def _move_to_baking_dish(self):
        print(f'Please move your ingredients in baking dish')

    def _open_oven(self):
        self.__is_open_oven = True
        print('Please open the oven')

    def _put_in_the_oven(self):
        self.__is_empty_oven = False
        print('Put ingredients in the oven')

    def _close_oven(self):
        self.__is_open_oven = False
        print('Please close the oven')

    def _turn_on_oven(self, oven_temperature: int):
        print('Turn on oven, set 200 degrees and wait 30 min')
        if oven_temperature > 180:
            print(
                f'Please reduce the temperature to 180 degrees. You set the temperature to {self.__oven_temperature} degrees')
        elif oven_temperature < 180:
            print(
                f'Please reduce the temperature to 180 degrees. You set the temperature to {self.__oven_temperature} degrees')
        else:
            print('Good job!!')

    def _waiting(self):
        time = 5
        while time != 0:
            if time > 1:
                print('Wait please')
            else:
                print('The pie is ready')
            time -= 1

    def _take_out_from_the_oven(self):
        print('Take your pie out of the oven.Bon appetit!')

    def _turn_off_oven(self):
        self.__oven_temperature = 0
        print('Please turn off your oven')
        print(
            f'Good job!The oven temperature is now set to {self.__oven_temperature} degrees and you can safely open '
            f'the oven')

    # Encapsulation
    def prepare_pie(self, milk: int, meal: int, egg: int, strawberry: int, oven_temperature: int):
        self._take_ingredients(milk, meal, egg, strawberry)
        self._mix_ingredients()
        self._move_to_baking_dish()
        self._open_oven()
        self._put_in_the_oven()
        self._close_oven()
        self._turn_on_oven(oven_temperature)
        self._waiting()
        self._turn_off_oven()
        self._open_oven()
        self._take_out_from_the_oven()
        self._close_oven()


if __name__ == '__main__':
    pie = Pie(300, 400, 2, 200, 180)
    pie.prepare_pie(300, 400, 2, 200, 180)
