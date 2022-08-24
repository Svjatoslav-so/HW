import datetime as dt
from typing import Union


class Stadium:

    def __init__(self, name: str, opening_date: Union[dt.date, list, tuple], country: str, city: str, capacity: int):
        if type(name) is str:
            self.__name = name
        else:
            raise TypeError("Name must be a str")

        if type(opening_date) is dt.date:
            self.__opening_date = opening_date
        elif type(opening_date) is tuple or type(opening_date) is list:
            self.__opening_date = dt.date(*opening_date)
        else:
            raise TypeError("Opening_date must be a list or tuple, for example (2012, 10, 25)")
        if self.__opening_date > dt.date.today():
            raise ValueError(f"This date has not yet arrived, today is {dt.date.today()}")

        if type(country) is str:
            self.__country = country
        else:
            raise TypeError("Country must be a str")

        if type(city) is str:
            self.__city = city
        else:
            raise TypeError("City must be a str")

        if type(capacity) is int:
            if capacity > 0:
                self.__capacity = capacity
            else:
                raise ValueError("Capacity must be greater than 0")
        else:
            raise TypeError("Capacity must be a int")

    def get_name(self) -> str:
        return self.__name

    def get_opening_date(self) -> dt.date:
        return self.__opening_date

    def get_country(self) -> str:
        return self.__country

    def get_city(self) -> str:
        return self.__city

    def get_capacity(self) -> int:
        return self.__capacity

    def set_name(self, name: str):
        if type(name) is str:
            self.__name = name
        else:
            raise TypeError("Name must be a str")

    def set_country(self, country: str):
        if type(country) is str:
            self.__country = country
        else:
            raise TypeError("Country must be a str")

    def set_city(self, city: str):
        if type(city) is str:
            self.__city = city
        else:
            raise TypeError("City must be a str")

    def set_capacity(self, capacity: int):
        if type(capacity) is int:
            if capacity > 0:
                self.__capacity = capacity
            else:
                raise ValueError("Capacity must be greater than 0")
        else:
            raise TypeError("Capacity must be a int")

    def __str__(self):
        return "Stadium object {}name: {}   opening_date: {}   country: {}   city: {}   capacity: {}{}" \
            .format("{", self.__name, self.__opening_date, self.__country, self.__city, self.__capacity, "}")


date = dt.date(1926, 9, 12)
stadium1 = Stadium("St_Name", (2012, 10, 25), "Ukraine", "City", 10)
stadium2 = Stadium("Трактор", date, "УССР", "Харьков", 5000)
stadium2.set_name("Металлист")
stadium2.set_country("Украина")
stadium2.set_capacity(40003)

print(stadium1.get_capacity())

print(stadium1)
print(stadium2)
