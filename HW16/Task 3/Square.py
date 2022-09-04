from Shape import Shape


class Square(Shape):
    _prefixes = "sq"
    # длина стороны квадрата
    __side = 0

    def __init__(self, x: float, y: float, side: float):
        # x,y - координаты левого верхнего угла квадрата
        super().__init__(x, y)
        self.set_side(side)

    def show(self) -> str:
        return super().show() + f" side: {self.__side}"

    def set_side(self, side: float):
        self.__side = Shape._check_value(side)

    def get_side(self) -> float:
        return self.__side
