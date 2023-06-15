from light_vehicles import LightVehicles


class Bike(LightVehicles):

    def __init__(self, count_wheels: int, count_of_doors: int, count_of_windows: int, engine_type: str,
                 place_of_movement: str, count_of_passengers: int, type_of_bike: str, wheel_diameter: float):
        super().__init__(count_wheels, count_of_doors, count_of_windows, engine_type, place_of_movement,
                         count_of_passengers)
        self._type_of_bike = type_of_bike
        self._wheel_diameter = wheel_diameter

    def bike_info(self):
        print(f'Type of bike is {self._type_of_bike} and  wheel diameter is {self._wheel_diameter}')
