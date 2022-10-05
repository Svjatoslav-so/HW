class Boat:
    __name: str  # headline
    __link: str  # link to boat page
    __price: str  # boat price
    __location: str  # boat location

    def __init__(self, name: str, price: str, link: str, location: str = ""):
        self.set_name(name)
        self.set_price(price)
        self.set_link(link)
        self.set_location(location)

    def set_name(self, name: str):
        if type(name) == str:
            self.__name = name
        else:
            self.__name = "Default Name"

    def set_link(self, link: str):
        if type(link) == str:
            self.__link = link
        else:
            self.__link = "Default Link"

    def set_price(self, price: str):
        if type(price) == str:
            self.__price = price
        else:
            self.__price = "$ 0.0"

    def set_location(self, location: str):
        if type(location) == str:
            self.__location = location
        else:
            self.__location = "Default Location"

    def __str__(self):
        return f"{self.__name} Price {self.__price}\nLink {self.__link}\nLocation {self.__location}"

    def __repr__(self):
        return f"<{self.__name} Price: {self.__price} Link: {self.__link} Location: {self.__location}>"

    def to_db(self) -> tuple[str, str, str, str]:
        return self.__name, self.__price, self.__link, self.__location
