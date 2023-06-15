from trucks import Trucks


class Crane(Trucks):

    def __init__(self, count_wheels: int, count_of_doors: int, count_of_windows: int, engine_type: str,
                 place_of_movement: str, load_capacity: int, presence_of_manipulator: bool):
        super().__init__(count_wheels, count_of_doors, count_of_windows, engine_type, place_of_movement, load_capacity)
        self._presence_of_manipulator = presence_of_manipulator

    def crane_info(self):
        if self._presence_of_manipulator:
            print(f'This crane has manipulator')
        else:
            print(f"This crane doesn't has manipulator")
