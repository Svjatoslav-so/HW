class Car:
    def __init__(self, model, manufacturer, year, price, engine_volume=None, color=None):
        if type(model) is str:
            self.__model_name = model
        else:
            raise TypeError("Model must be a str")

        if type(manufacturer) is str:
            self.__manufacturer = manufacturer
        else:
            raise TypeError("Manufacturer must be a str")

        if type(year) is int:
            if year > 1980:
                self.__release_year = year
            else:
                raise ValueError("Year must be greater than 1980")
        else:
            raise TypeError("Year must be a int")

        if engine_volume is None or type(engine_volume) is float:
            if engine_volume is None or engine_volume > 0:
                self.__engine_volume = engine_volume
            else:
                raise ValueError("Engine_volume must be greater than 0")
        else:
            raise TypeError("Engine_volume must be a float")

        if color is None or type(color) is str:
            self.__car_color = color
        else:
            raise TypeError("Color must be a str")

        if price is None or type(price) is float:
            if price is None or price > 0:
                self.__price = price
            else:
                raise ValueError("Price must be greater than 0")
        else:
            raise TypeError("Price must be a float")

    def get_model_name(self):
        return self.__model_name

    def get_release_year(self):
        return self.__release_year

    def get_manufacturer(self):
        return self.__manufacturer

    def get_engine_volume(self):
        return self.__engine_volume

    def get_car_color(self):
        return self.__car_color

    def get_price(self):
        return self.__price

    def set_car_color(self, color):
        if color is None or type(color) is str:
            self.__car_color = color
        else:
            raise TypeError("Color must be a str")

    def set_engine_volume(self, engine_volume):
        if engine_volume is None or type(engine_volume) is float:
            if engine_volume is None or engine_volume > 0:
                self.__engine_volume = engine_volume
            else:
                raise ValueError("Engine_volume must be greater than 0")
        else:
            raise TypeError("Engine_volume must be a float")

    def set_price(self, price):
        if price is None or type(price) is float:
            if price is None or price > 0:
                self.__price = price
            else:
                raise ValueError("Price must be greater than 0")
        else:
            raise TypeError("Price must be a float")

    def __str__(self):
        return f"""class Car:
    model_name:   {self.__model_name}
    manufacturer: {self.__manufacturer}
    release_year: {self.__release_year}
    engine_volume:{self.__engine_volume}
    car_color:    {self.__car_color}
    price:        {self.__price}"""


car1 = Car("N6", "Volvo", 2010, 40000.0)
print(car1)
print(car1.__dir__())
car2 = Car("123", "32", 1981, 1.0, 0.8, "1")
car2.set_car_color(None)
car2.set_price(None)
car2.set_engine_volume(2.0)
# Немного читерства
car2._Car__model_name = "Model S"
car2._Car__manufacturer = "Tesla"
print(car1._Car__manufacturer)
print(car2)
