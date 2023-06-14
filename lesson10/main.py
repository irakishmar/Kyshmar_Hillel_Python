from plane import Plane
from helicopter import Helicopter
from cars import Cars
from bike import Bike
from crane import Crane
from tractor import Tractor

if __name__ == '__main__':
    plane_example = Plane(2, 2, 24, 'disel', 'wings', 'air', 8)
    plane_example.plane_info()
    plane_example.flying_vehicle_info()

    print('-' * 100)

    helicopter_example = Helicopter(3, 2, 3, 'disel', 'rotor', 'air', 4)
    helicopter_example.helicopter_info()
    helicopter_example.flying_vehicle_info()

    print('-' * 100)

    car_example = Cars(4, 4, 4, 'petrol', 'ground', 4, 'Mazda', 'Hatchback')
    car_example.cars_info()
    car_example.light_vehicles_info()
    car_example.ground_vehicle_info()

    print('-' * 100)

    bike_example = Bike(2, 0, 0, 'electric', 'ground', 1, 'sport bike', 24.5)
    bike_example.bike_info()
    bike_example.light_vehicles_info()
    bike_example.ground_vehicle_info()

    print('-' * 100)

    crane_example = Crane(4, 2, 3, 'disel', 'ground', 20, True)
    crane_example.crane_info()
    crane_example.trucks_info()
    crane_example.ground_vehicle_info()

    print('-' * 100)

    tractor_example = Tractor(4, 1, 3, 'disel', 'ground', 40, True)
    tractor_example.tractor_info()
    tractor_example.trucks_info()
    tractor_example.ground_vehicle_info()