# class Person:
#
#     def __init__(self, name):
#         self.__name = name


#     @property
#     def name(self):
#         return self.__name
#
#
#     def display_info(self):
#         print(f"Name:{self.__name}")


# class Employee(Person):
#
#     def work(self):
#         print(f"{self.name} works")
#
# Igor = Employee("Igor")
# print(Igor.name)
# Igor.display_info()
# Igor.work()


# class Person:
#
#     def __init__(self, name):
#         self.__name = name

#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f"Name:{self.__name}")
#

#
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#
#     def name(self):
#         return self.__name
#
#     def age(self):
#         return self.__age
#
#     def display_info(self):
#         print(f"Name: {self.__name} Age:{self.__age}")
#
# Igor = Person("Igor", 21)
# print(Igor.name)
# Igor.display_info()
#

class Employee:
    def work(self):
        print("Employee works")


class User:
    def users(self):
        print("User test")

class WorkingUser(Employee, User):
    pass


print(WorkingUser.__mro__)
# Igor = WorkingUser()
# Igor.work()
# Igor.users()


