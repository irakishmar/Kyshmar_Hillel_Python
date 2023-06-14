from flying_vehicle import FlyingVehicle


class Plane(FlyingVehicle):

    def __init__(self, count_wheels: int, count_of_doors: int, count_of_windows: int, engine_type: str,
                 aerodynamic_elements: str, place_of_movement: str, count_of_turbines: int):
        super().__init__(count_wheels, count_of_doors, count_of_windows, engine_type, aerodynamic_elements,
                         place_of_movement)
        self._count_of_turbines = count_of_turbines

    def move(self):
        pass

    def plane_info(self):
        print(f'The plane has {self._count_of_turbines} turbines')
