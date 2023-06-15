from ground_vehicle import GroundVehicle


class Trucks(GroundVehicle):

    def __init__(self, count_wheels: int, count_of_doors: int, count_of_windows: int, engine_type: str,
                 place_of_movement: str, load_capacity: int):
        super().__init__(count_wheels, count_of_doors, count_of_windows, engine_type, place_of_movement)
        self._load_capacity = load_capacity

    def trucks_info(self):
        print(f'This vehicle has {self._load_capacity} tons of load capacity')
