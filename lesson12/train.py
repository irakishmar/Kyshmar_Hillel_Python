class Train:
    def __init__(self, locomotive, num_of_wagon):
        self.__locomotive = locomotive
        self.__num_of_wagon = num_of_wagon
        self.__count_of_wagons = []

    def __len__(self):
        self.__count_of_wagons = []
        for wagon_number in range(1, self.__num_of_wagon + 1):
            self.__count_of_wagons.append(wagon_number)
        return len(self.__count_of_wagons)

    def __str__(self):
        self.__len__()
        result = len(self.__count_of_wagons)
        wagon_list = '-'.join(f'[{wagon_number}]' for wagon_number in self.__count_of_wagons)
        return f'The tarin has {result} wagons \n<==[{self.__locomotive}]-{wagon_list}'


class Wagon:
    def __init__(self, number_of_wagon):
        self.__number_of_wagon = number_of_wagon
        self.__passengers = []

    def add_passenger(self, passenger):
        if len(self.__passengers) < 5:
            self.__passengers.append(passenger)
        else:
            print(f"Wagon {self.__number_of_wagon} is full. Please choose another wagon.")

    def __len__(self):
        return len(self.__passengers)

    def __str__(self):
        self.__len__()
        if self.__len__() > 0:
            count_of_passengers = f'{self.__class__.__name__} {self.__number_of_wagon} contain {self.__len__()} passengers: {self.__passengers}'
        else:
            count_of_passengers = f'The {self.__class__.__name__} {self.__number_of_wagon} is empty'
        return count_of_passengers


if __name__ == '__main__':
    train = Train('Head', 3)
    print(str(train))

    wagon_1 = Wagon(1)
    wagon_2 = Wagon(2)
    wagon_3 = Wagon(3)

    wagon_1.add_passenger("Passenger 1")
    wagon_1.add_passenger("Passenger 2")
    wagon_1.add_passenger("Passenger 3")
    wagon_1.add_passenger("Passenger 4")
    wagon_1.add_passenger("Passenger 5")
    wagon_1.add_passenger("Passenger 6")

    wagon_2.add_passenger("Passenger 4")
    wagon_2.add_passenger("Passenger 5")
    wagon_2.add_passenger("Passenger 6")

    print(str(wagon_1))
    print(str(wagon_2))
    print(str(wagon_3))
