from light_vehicles import LightVehicles


class Cars(LightVehicles):

    def __init__(self, count_wheels: int, count_of_doors: int, count_of_windows: int, engine_type: str,
                 place_of_movement: str, count_of_passengers: int, brand: str, type_of_car: str):
        super().__init__(count_wheels, count_of_doors, count_of_windows, engine_type, place_of_movement,
                         count_of_passengers)
        self._brand = brand
        self._type_of_car = type_of_car

    def cars_info(self):
        print(f'Brand of car is {self._brand}, type of car is {self._type_of_car}')
