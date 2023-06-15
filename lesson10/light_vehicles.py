from ground_vehicle import GroundVehicle


class LightVehicles(GroundVehicle):

    def __init__(self, count_wheels: int, count_of_doors: int, count_of_windows: int, engine_type: str,
                 place_of_movement: str, count_of_passengers: int):
        super().__init__(count_wheels, count_of_doors, count_of_windows, engine_type, place_of_movement)
        self._count_of_passengers = count_of_passengers

    def light_vehicles_info(self):
        print(f'This vehicle can carry {self._count_of_passengers} passengers')
