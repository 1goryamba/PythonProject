class Person:
    type = "Person"
    description = "Describes a person"

print(Person.type)
print(Person.description)

Person.type = "Class Person"
print(Person.type)
from symtable import Class

class Person:
    type = "Person"
    def __init__(self, name):
        self.name = name

Igor = Person("Igor")
print(Igor.type)

Person.type = "Class person"
print(Igor.type)

class Person:
    default_name = "Undefined"

    def __init__(self,name):
        if name:
            self.name = name
        else:
            self.name = Person.default_name

Igor = Person("Igor")
Igor = Person ("")
print(Igor.name)

class Person:
    name = "Undefined"

    def print_name(self):
        print(self.name)

Igor = Person()
# Igor.print_name()
Igor.name = "Igor"
Igor.print_name()

class Person:
    __type = "Person"

    @staticmethod
    def print_type():
        print(Person.__type)

Person.print_type()