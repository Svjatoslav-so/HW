from Figure import Figure


class Rectangle(Figure):
    __side1 = 0
    __side2 = 0

    def __init__(self, side1: float, side2: float):
        self.__side1 = Figure._check_value(side1)
        self.__side2 = Figure._check_value(side2)

    def get_square(self) -> float:
        return self.__side1 * self.__side2

    def __str__(self):
        return f"Rectangle object [side1: {self.__side1} side2: {self.__side2}]"
