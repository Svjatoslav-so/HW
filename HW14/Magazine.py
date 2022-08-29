from typing import Union
import re

from Book import Book


class Magazine(Book):
    __ages = {18, 16, 12, 6, 0}

    # номер журнала
    __number = 1
    # тип обложки
    __cover_type = "Мягкая обложка"
    # возрастные ограничения
    __age_restrictions = 18
    # международный стандартный сериальный номер
    __issn = 30178471

    def __init__(self, title: str, author: str, publishing_house: str, year: int,
                 price: Union[float, None], number: int, cover_type: str, age_restrictions: int, issn: int):
        super().__init__(title, author, publishing_house, year, "magazine", price)
        self.set_number(number)
        self.set_cover_type(cover_type)
        self.set_age_restrictions(age_restrictions)
        self.set_issn(issn)

    def get_number(self) -> int:
        return self.__number

    def get_cover_type(self) -> str:
        return self.__cover_type

    def get_age_restrictions(self) -> int:
        return self.__age_restrictions

    def get_issn(self) -> int:
        return self.__issn

    def set_number(self, number: int):
        if type(number) is int:
            if number > 0:
                self.__number = number
            else:
                raise ValueError("Number must be greater than 0")
        else:
            raise TypeError("Number must be a int")

    def set_cover_type(self, cover_type: str):
        if type(cover_type) is str:
            self.__cover_type = cover_type
        else:
            raise TypeError("Cover_type must be a str")

    def set_age_restrictions(self, age_restrictions: int):
        if type(age_restrictions) is int:
            if age_restrictions in self.__ages:
                self.__age_restrictions = age_restrictions
            else:
                raise ValueError("Age_restrictions must be one of (18, 16, 12, 6, 0)")
        else:
            raise TypeError("Age_restrictions must be a int")

    def set_issn(self, issn: int):
        if type(issn) is int:
            if issn / 100000000 < 1:
                self.__issn = issn
            else:
                raise ValueError("ISSN must be an eight digit number")
        else:
            raise TypeError("ISSN must be a int")

    def __str__(self) -> str:
        return f" class Magazine [" + re.search(r"\[(.*)\]", super().__str__()).group(1) \
               + f"   number: {self.__number}   cover_type: \"{self.__cover_type}\"   age_restrictions: " \
                 f"{self.__age_restrictions}+   issn: {self.__issn:08}]"


magazine = Magazine("Yachting World", "Elaine Bunting", "TI Media", 2013, 200., 13, "soft cover", 16, 727479)
print(magazine)

