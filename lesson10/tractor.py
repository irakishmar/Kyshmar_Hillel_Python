from trucks import Trucks


class Tractor(Trucks):

    def __init__(self, count_wheels: int, count_of_doors: int, count_of_windows: int, engine_type: str,
                 place_of_movement: str, load_capacity: int, presence_of_bucket: bool):
        super().__init__(count_wheels, count_of_doors, count_of_windows, engine_type, place_of_movement, load_capacity)
        self._presence_of_bucket = presence_of_bucket

    def tractor_info(self):
        if self._presence_of_bucket:
            print(f'This crane has tractor bucket')
        else:
            print(f"This crane doesn't has tractor bucket")
