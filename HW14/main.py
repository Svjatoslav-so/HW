class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"Person object name:{self.name}   surname: {self.surname}   age: {self.age}"


class Student(Person):
    # spec = "Agrarnoe delo"
    def __init__(self, name, surname, age, spec):
        self.spec = spec
        super().__init__(name,surname,age)


    def isSuccesful(self, mean_score):
        return True if mean_score > 75 else False

    def __str__(self):
        # return Person.__str__(self)+f" spec: {self.spec}"
        return super().__str__() + f" spec: {self.spec}"


p1 = Person("Vaselisa", "Mikulishna", 29)
print(p1)

s1 = Student("Petr", "Muromskiy", 21, "Agrarnoe delo")
print(s1)
