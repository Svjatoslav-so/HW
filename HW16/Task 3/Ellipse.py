from Shape import Shape


class Ellipse(Shape):
    _prefixes = "el"
    # длины сторон описанного прямоугольника
    __side1 = 0
    __side2 = 0

    def __init__(self, x: float, y: float, side1: float, side2: float):
        # x,y - координаты верхнего угла описанного вокруг эллипса прямоугольника
        super().__init__(x, y)
        self.set_sides(side1, side2)

    def show(self) -> str:
        return super().show() + f" side1: {self.__side1} side2: {self.__side2}"

    def set_sides(self, side1: float, side2: float):
        self.__side1 = Shape._check_value(side1)
        self.__side2 = Shape._check_value(side2)

    def get_sides(self) -> tuple[float, float]:
        return self.__side1, self.__side2
