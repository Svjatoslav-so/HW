import re
from Book import Book


class Newspaper(Book):
    # Тематика
    __topic = "кроссворды"
    # Периодичность издания
    __periodicity = "1 раз в месяц"
    # Тираж
    __circulation = 10000
    # Язык
    __language = "русский"

    def __init__(self, title, author, publishing_house, year, price,
                 topic, periodicity, circulation, language):
        super().__init__(title, author, publishing_house, year, "newspaper", price)
        self.set_topic(topic)
        self.set_periodicity(periodicity)
        self.set_circulation(circulation)
        self.set_language(language)

    def get_topic(self):
        return self.__topic

    def get_periodicity(self):
        return self.__periodicity

    def get_circulation(self):
        return self.__circulation

    def get_language(self):
        return self.__language

    def set_topic(self, topic):
        self.__topic = topic

    def set_periodicity(self, periodicity):
        self.__periodicity = periodicity

    def set_circulation(self, circulation):
        if type(circulation) is int:
            if circulation > 0:
                self.__circulation = circulation
            else:
                raise ValueError("Circulation must be greater than 0")
        else:
            raise TypeError("Circulation must be a int")

    def set_language(self, language):
        self.__language = language

    def __str__(self):
        return f" class Newspaper [" + re.search(r"\[(.*)\]", super().__str__()).group(1)\
               + f"   topic: \"{self.__topic}\"   periodicity: \"{self.__periodicity}\"   circulation: " \
                 f"\"{self.__circulation}\"   language: \"{self.__language}\"]"


newp = Newspaper("Вечерний Харьков", "ЕЛЕНА ШЕВЧУК", 'ООО "Редакция газеты "Вечерний Харьков"', 2022, 2.0, "новости",
                 "3 раза в неделю", 120024, "украинский, русский")
print(newp)
