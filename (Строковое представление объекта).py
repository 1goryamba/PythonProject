class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name:{self.name} Age: {self.age}")

    def __str__(self):
        return f"Name:{self.name} Age: {self.age}"

I = Person("Igor", 21)
print(I)
# I.display_info()