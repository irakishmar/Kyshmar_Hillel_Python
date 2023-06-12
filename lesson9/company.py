class Company:
    """
    Description of the Company class using getters, setters, static methods and class methods
    """

    def __init__(self, name: str, count_of_employee: int, founding_date: str, main_office: str, budget: float,
                 actual_info_year: int):
        self.__name = name
        self.__count_of_employee = count_of_employee
        self.__founding_date = founding_date
        self.__main_office = main_office
        self.__budget = budget
        self.__actual_info_year = actual_info_year

    @property
    def name(self):
        return self.__name

    @property
    def founding_date(self):
        return self.__founding_date

    @property
    def main_office(self):
        return self.__main_office

    @property
    def count_of_employee(self):
        return self.__count_of_employee

    @count_of_employee.setter
    def count_of_employee(self, new_count):
        if isinstance(new_count, int) and new_count > 0:
            self.__count_of_employee = new_count
        else:
            raise TypeError(f'Count of employee should be an integer and greater than 0')

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, new_budget):
        if isinstance(new_budget, int) and new_budget > 0:
            self.__budget = new_budget
        else:
            raise TypeError(f'Budget value should be an integer and greater than 0')

    @property
    def actual_info_year(self):
        return self.__actual_info_year

    @actual_info_year.setter
    def actual_info_year(self, new_actual_info_year):
        if isinstance(new_actual_info_year, int) and new_actual_info_year > 0:
            self.__actual_info_year = new_actual_info_year
        else:
            raise TypeError(f'Actual year value should be an integer and greater than 0')

    @staticmethod
    def info_about_company():
        print("Google is an American multinational corporation, reorganized on October 15, 2015 into "
              "the international conglomerate Alphabet Inc., a company within the Alphabet holding "
              "investing in Internet search, cloud computing and advertising technologies. The company was founded by"
              " Larry Page and Sergey Brin.")

    @classmethod
    def formating_date(cls, name: str, count_of_employee: int, founding_date: str, main_office: str, budget: float,
                       actual_info_year: int):

        month_dict = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
                      '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November',
                      '12': 'December'}

        new_data = founding_date.split('.')
        for key in month_dict:
            if new_data[1] == key:
                new_data[1] = month_dict[key]
                break
        formatted_date = ' '.join(new_data)

        # formatted_date = new_data
        return cls(name, count_of_employee, formatted_date, main_office, budget,
                   actual_info_year)

    def display_common_info(self):
        print(f'Common information about {self.__name}:')
        print(f'Name of company: {self.__name}')
        print(f'Founding date of {self.__name} company: {self.__founding_date}')
        print(f'Main office of {google.name} company: {self.__main_office}')
        print('-' * 100)

    def display_uptodate_info(self):
        print(f'Up-to-date information for {self.__actual_info_year}:')
        print(f'The number of employees for {self.__actual_info_year} is: {self.__count_of_employee}')
        print(f"The company's budget for {self.__actual_info_year} is: {self.__budget}")
        print('-' * 100)


if __name__ == '__main__':
    google = Company('Google', 140000, '4.09.1998', 'Mountain View, California, USA', 2000000000000, 2023)

    formatted_date = Company.formating_date('Google', 140000, '4.09.1998', 'Mountain View, California, USA',
                                            2000000000000, 2023)

    Company.info_about_company()
    formatted_date.display_common_info()
    google.display_uptodate_info()

    google.count_of_employee = 130120
    google.budget = 1000000876543
    google.actual_info_year = 2022

    google.display_uptodate_info()