class Book:

    def __init__(self, title, author, publishing_house, year, genre, price):
        if type(title) is str:
            self.__title = title
        else:
            raise TypeError("Title must be a str")

        if type(author) is str:
            self.__author = author
        else:
            raise TypeError("Author must be a str")

        if type(publishing_house) is str:
            self.__publishing_house = publishing_house
        else:
            raise TypeError("Publishing_house must be a str")

        if type(year) is int:
            if year > 2000:
                self.__year = year
            else:
                raise ValueError("Year must be greater than 2000")
        else:
            raise TypeError("Year must be a int")

        if type(genre) is str:
            self.__genre = genre
        else:
            raise TypeError("Genre must be a str")

        if price is None or type(price) is float:
            if price is None or price > 0:
                self.__price = price
            else:
                raise ValueError("Price must be greater than 0")
        else:
            raise TypeError("Price must be a float")

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publishing_house(self):
        return self.__publishing_house

    def get_year(self):
        return self.__year

    def get_genre(self):
        return self.__genre

    def get_price(self):
        return self.__price

    def set_genre(self, genre):
        if type(genre) is str:
            self.__genre = genre
        else:
            raise TypeError("Genre must be a str")

    def set_price(self, price):
        if price is None or type(price) is float:
            if price is None or price > 0:
                self.__price = price
            else:
                raise ValueError("Price must be greater than 0")
        else:
            raise TypeError("Price must be a float")

    def add_genre(self, genre):
        if type(genre) is str:
            self.__genre += ", " + genre
        else:
            raise TypeError("Genre must be a str")

    def __str__(self):
        return f" class Book [ title: \"{self.__title}\"   author: \"{self.__author}\"   " \
               f"publishing_house: \"{self.__publishing_house}\"   year: {self.__year}   " \
               f"genre: \"{self.__genre}\"   price: {self.__price}]"


book = Book("MyFirstBook", "I'm", "My PubHouse", 2002, "My genre", 0.1)
book.set_price(12.0)
book.add_genre("New genre")
print(book)
