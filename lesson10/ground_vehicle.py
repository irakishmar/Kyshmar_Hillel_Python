from transport import Transport


class GroundVehicle(Transport):

    def __init__(self, count_wheels: int, count_of_doors: int, count_of_windows: int, engine_type: str,
                 place_of_movement: str):
        super().__init__(count_wheels, count_of_doors, count_of_windows, engine_type)
        self._place_of_movement = place_of_movement

    def move(self):
        pass

    def ground_vehicle_info(self):
        if self._count_of_doors > 0 and self._count_of_windows:
            print(f'This ground vehicle has {self._count_of_doors} doors, {self._count_of_windows} windows and '
                  f'moves on the {self._place_of_movement}')
        else:
            print(f'This ground vehicle moves on the {self._place_of_movement}')
