from datetime import datetime


class Worker:
    '''
        Description of the Worker class using getters, setters, static methods and class methods
    '''

    def __init__(self, name: str, birth_year: int, salary: float, age: int):
        self.__name = name
        self.__birth_year = birth_year
        self.__salary = salary
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise TypeError(f'Name of worker  should be a string')

    @property
    def birth_year(self):
        return self.__birth_year

    @birth_year.setter
    def birth_year(self, new_birth_year):
        if isinstance(new_birth_year, int) and 1953 <= new_birth_year <= 2005:
            self.__birth_year = new_birth_year
        else:
            raise TypeError(
                f'Birth year value should be an integer and the person should be between 18 and 60 years of age')

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if isinstance(new_salary, int) and new_salary > 0:
            self.__salary = new_salary
        else:
            raise TypeError(f'Salary value should be an integer and greater than 0')


    @classmethod
    def age_employee(cls, name: str, birth_year: int, salary: float):
        age = (cls.__calculate_age()) - birth_year
        return cls(name, birth_year, salary, age)

    @staticmethod
    def __calculate_age():
        current_year = datetime.now().year
        return current_year

    def display_info_employee(self):
        print('Employee:')
        print(f'Name of employee: {self.__name}')
        print(f'Birth year of employee: {self.__birth_year}')
        print(f'Salary of employee: {self.__salary}')
        print(f'Age of employee: {self.__age} years')


if __name__ == '__main__':
    employee = Worker.age_employee('Sten', 1992, 1500)
    employee.display_info_employee()

    print('-' * 100)

    employee.name = 'Cati'
    employee.birth_year = 1998
    employee.salary = 2000

    birth_day_second_employee = Worker.age_employee('Cati', 1998, 2000)
    birth_day_second_employee.display_info_employee()