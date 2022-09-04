import re


class Shape:
    # приставка используется при текстовом представлении фигуры в качестве идентификатора
    _prefixes = "sh"  # необходимо переопределять в классах наследниках
    # координаты фигуры
    __x = 0
    __y = 0

    def __init__(self, x: float, y: float):
        self.set_x(x)
        self.set_y(y)

    # возвращает строковое представление фигуры
    def show(self) -> str:  # необходимо переопределять в классах наследниках
        return f"{self._prefixes} x: {self.__x} y: {self.__y}"

    # записывает строковое представление фигуры в файл
    def save(self, file, mode="w"):
        with open(file, mode) as f:
            f.write(self.show() + "\n")

    # возвращает список фигур загруженных из файла file
    @classmethod
    def load(cls, file: str, ):
        shapes_list = []
        with open(file, "r") as f:
            all_shapes = f.readlines()
            for line in all_shapes:
                if line.startswith(cls._prefixes):
                    match_list = re.findall(r"\d\.\d*", line)
                    # print("len", len(match_list))
                    shapes_list.append(cls(*match_list))
        return shapes_list

    # проверяет чтобы значение было приводимо к float и было больше 0
    @staticmethod
    def _check_value(value) -> float:
        value = abs(float(value))
        if value == 0:
            raise ValueError("This value cannot be less than or equal to 0")
        return value

    def set_x(self, x: float):
        self.__x = Shape._check_value(x)

    def set_y(self, y: float):
        self.__y = Shape._check_value(y)

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y
