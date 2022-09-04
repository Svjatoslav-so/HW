import math

from Figure import Figure


class Circle(Figure):
    __radius = 0

    def __init__(self, radius: float):
        self.__radius = Figure._check_value(radius)

    def get_square(self) -> float:
        return math.pi * self.__radius ** 2

    def __str__(self):
        return f"Circle object [radius {self.__radius}]"
