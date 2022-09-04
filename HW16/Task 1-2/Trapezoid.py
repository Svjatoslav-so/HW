from Figure import Figure


class Trapezoid(Figure):
    __base1 = 0
    __base2 = 0
    __height = 0

    def __init__(self, base1: float, base2: float, height: float):
        self.__base1 = Figure._check_value(base1)
        self.__base2 = Figure._check_value(base2)
        self.__height = Figure._check_value(height)

    def get_square(self) -> float:
        return (self.__base1 + self.__base2) * 0.5 * self.__height

    def __str__(self):
        return f"Trapezoid object [base1: {self.__base1} base2: {self.__base2} height: {self.__height}]"
