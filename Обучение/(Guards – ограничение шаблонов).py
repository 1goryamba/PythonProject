class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def enter(person):
    match person:
        case Person(name=name, age=age) if age < 18:
            print(f"{name}, доступ запрещен")
        case Person(name=name):
            print(f"{name}, добро пожаловать")

enter(Person("Igor", 21))
enter(Person("NotIgor", 17))

def check_data(data):
    match data:
        case name, age if name == "admin" or age not in range (1, 101):
            print("Некорректное значение")
        case name, age:
            print(f"Данные проверены. Name: {name} Age: {age}")

check_data(("admin", -1))
check_data(("Igor", 21))