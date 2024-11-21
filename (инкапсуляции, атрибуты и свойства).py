class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person(self):
        print(f"Имя: {self.name}\tВозраст: {self.age}")
        return self

Person("Igor",21).print_person()

Igor = Person("I", 21)
Igor.name = "Igor"
Igor.age = 21

Igor.print_person()


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_age(self, age):
        if 0 < age < 110:
            self.__age = age
        else:
            print("Invalid age")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def print_person(self):
        print(f"Имя:{self.__name}\tВозраст: {self.__age}")

Igor = Person("Igor",21)
Igor.print_person()
Igor.set_age(-10)
