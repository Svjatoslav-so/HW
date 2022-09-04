from Figure import Figure


class RightTriangle(Figure):
    __leg1 = 0
    __leg2 = 0

    def __init__(self, cathetus1: float, cathetus2: float):
        self.__leg1 = Figure._check_value(cathetus1)
        self.__leg2 = Figure._check_value(cathetus2)

    def get_square(self) -> float:
        return 0.5 * self.__leg1 * self.__leg2

    def __str__(self):
        return f"RightTriangle object [cathetus1: {self.__leg1} cathetus2: {self.__leg2}]"
