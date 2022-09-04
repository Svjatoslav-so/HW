from Shape import Shape


class Circle(Shape):
    _prefixes = "ci"
    # радиус
    __radius = 0

    def __init__(self, x: float, y: float, radius: float):
        # x,y - координаты центра окружности
        super().__init__(x, y)
        self.set_radius(radius)

    def show(self) -> str:
        return super().show() + f" radius: {self.__radius}"

    def set_radius(self, radius: float):
        self.__radius = Shape._check_value(radius)

    def get_radius(self) -> float:
        return self.__radius
