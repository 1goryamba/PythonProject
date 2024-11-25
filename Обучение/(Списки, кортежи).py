# numbers = [1,2,3]
# people = ("P1", "P2", "P3")
# numbers1 = []
# numbers2 = list()

# objects = (1, "Hello", 2.6, True)

# numbers1 = [1,2,3]
# numbers2 = list(numbers1)
# print(numbers2)

# letters = list("Hi")
# print(letters)

# people = ("P1", "P2", "P3")

# print(numbers)
# print(people)

# people = ("N", "I", "S")
# for person in people:
#     print(person)

# people = ["p1", "p2", "p3"]
# for person in people:
#     print(person)

# people = ["p1", "p2", "p3"]
# i = 0
# while i < len(people):
#     print(people[i])
#     i += 1

# numbers1 = (1, 2, 3, 4, 5)
# numbers2 = list[(1, 2, 3, 4, 5)]
# if numbers1 == numbers2:
#     print("numbers1 equal to numbers2")
# else:
#     print("numbers1 is not equal to numbers2")

# nums = [10, 20, 30, 40, 50]
# nums[1:4]=[11, 22]
# print(nums)

# people = ["A", "B", "C"]
# people.sort()
# people.reverse() # отвечает за обратный порядок отображения данных
# print(people)

# filter(fun, iter)

# numbers = [-5, -3, -1, 0, 5]
#
# def condition(number): return number > 1
#
# result = filter(condition, numbers)
#
# for n in result: print(n, end ="")

# map(fun, iter)

# numbers = [1, 3, 5]
#
# def square(number): return number * numbers
#
# result = map(square, numbers)
#
# for n in result: print(n, end = "")

# numbers = [1, 3, 5]
#
# result = map(lambda n: n * n, numbers)
#
# for n in result:print(n, end = "")
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# people = [Person ("I", 21), Person ("N", 22), Person ("S", 23)]
#
# view = map(lambda p: p.name, people)
#
# for person in view:
#     print(person)

# numbers = (1,3,5,100,950,1500)
# print(min(numbers))
# print(max(numbers))

# people1 = ("I1", "I2", "I3")
# people2 = ("I4", "I5", "I6")
# people3 = people1 + people2
# print(people3)

people = [
    ["I1", 21],
    ["I2", 22],
    ["I3", 23]
]
print(people[0])
print(people[0][0])
print(people[0][1])
