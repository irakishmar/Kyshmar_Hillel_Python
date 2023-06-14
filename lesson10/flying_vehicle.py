from transport import Transport


class FlyingVehicle(Transport):

    def __init__(self, count_wheels: int, count_of_doors: int, count_of_windows: int, engine_type: str,
                 aerodynamic_elements: str, place_of_movement: str):
        super().__init__(count_wheels, count_of_doors, count_of_windows, engine_type)
        self._aerodynamic_elements = aerodynamic_elements
        self._place_of_movement = place_of_movement

    def move(self):
        pass

    def flying_vehicle_info(self):
        print(
            f'This flying vehicle has aerodynamic elements: {self._aerodynamic_elements}, {self._count_of_doors} doors'
            f' and {self._count_of_windows} windows')
