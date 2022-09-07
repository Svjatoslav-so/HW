import functools
from typing import Type, TypeVar  # , Union


class Person:
    __firstname: str
    __lastname: str
    __phone: str

    def __init__(self, firstname: str, lastname: str, phone: str):
        self.set_firstname(firstname)
        self.set_lastname(lastname)
        self.set_phone(phone)

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_phone(self):
        return self.__phone

    def set_firstname(self, firstname: str):
        self.__firstname = firstname.capitalize()

    def set_lastname(self, lastname: str):
        self.__lastname = lastname.capitalize()

    def set_phone(self, phone: str):
        self.__phone = phone

    def __str__(self) -> str:
        attr_values_list = [self.__getattribute__(attr) for attr in self.__dict__.keys()]
        return f'{self.__class__.__name__} {functools.reduce(lambda x, y: str(x) + " " + str(y), attr_values_list)}'

    def __repr__(self) -> str:
        attr_pair_list = [attr + ": " + str(self.__getattribute__(attr)) for attr in self.__dict__.keys()]
        return f'{self.__class__.__name__} {functools.reduce(lambda x, y: x + "    " + y, attr_pair_list)}'

    def to_file(self, filename: str):
        with open(filename, 'a') as file:
            file.write(self.__str__() + '\n')

    T = TypeVar("T", bound="Person")

    @classmethod
    # def from_file(cls: Type["Person"], filename: str) -> list[Union["Person", "Student", "Teacher"]]:
    def from_file(cls: Type[T], filename: str) -> list[T]:
        new_objs = []
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                values = line.split()
                obj_cls, args = values[0], values[1:]
                if cls.__name__ == obj_cls:
                    new_objs.append(cls(*args))
        return new_objs


class Student(Person):
    __group = ""

    def __init__(self, firstname: str, lastname: str, phone: str, group: str):
        super().__init__(firstname, lastname, phone)
        self.set_group(group)

    def get_group(self) -> str:
        return self.__group

    def set_group(self, group: str):
        self.__group = group


class Teacher(Person):
    __subject = ""

    def __init__(self, firstname: str, lastname: str, phone: str, subject: str):
        super().__init__(firstname, lastname, phone)
        self.set_subject(subject)

    def get_subject(self) -> str:
        return self.__subject

    def set_subject(self, subject: str):
        self.__subject = subject


with open("test.txt", "w") as f:
    pass

li = [Student('Ivasyk', 'Bulkin', 'trinolyatrulyalya', 'Python11'),
      Student('Grigoiy', 'Terkin', '+387415874165', 'Python21'),
      Student('Anna', 'Chechetkina', '+04478451235', 'C++14'),
      Student('Svetlana', 'Bulkina', 'trinolyatrulyalya2', 'Python11'),
      Student('Anatloiy', 'Fedorov', '0991234756', 'C++17'),
      Person('Vasya', ' Pupkin', 'trinolyatrulyalya'),
      Person('Gora', 'Tereshkin', '+3874159767165'),
      Person('Angelina', 'Cherkashena', '+04409451235'),
      Teacher('Olena', 'Vilka', 'trinolyatrulyalya2', 'English'),
      Teacher('Oksana', 'Shmaly', '0991234756', 'Programming')]

for i in li:
    i.to_file('test.txt')
objs = Person.from_file('test.txt') + Student.from_file('test.txt') + Teacher.from_file('test.txt')
for obj in objs:
    print(obj)
