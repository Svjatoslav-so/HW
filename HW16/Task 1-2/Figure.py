class Figure:
    @staticmethod
    def _check_value(value) -> float:
        value = abs(float(value))
        if value == 0:
            raise ValueError("This value cannot be less than or equal to 0")
        return value

    def get_square(self) -> float:
        return 0

    def __int__(self):
        return int(self.get_square())
