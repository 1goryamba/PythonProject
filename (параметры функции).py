# def test(name):
#     print(f"Hello, {name}")
#
#
# test("1")
# test("2")
# test("3")

# def person(name, age):
#     print (f"name: {name}")
#     print (f"age: {age}")
#
# person("Igor", 21)

# def test(name="h"):
#     print(f"hello, {name}")
#
# test()
# test("p")

# def test(name, age = 18):
#     print (f"name: {name} age {age}")
#
# test("Igor", 21)
#
# def person (name = "Igor", age = 21):
#     print (f"name:{name} age: {age}")
#
#
# person()
# person("Bob")
# person("Tom", 21)

# def person (name, age):
#     print(f"name:{name} age: {age}")
#
#
# person(age= 21, name = "Igor")

# def person(name,age):
#     print (f"name:{name} age {age}")
#
# person(age = 21, name = "Igor")

# def person (name, *, age, company):
#     print (f"name: {name} age: {age} company: {company}")
#
# person ("Igor", age = 21, company= "TESLA")


# def sum(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     print(f"sum = {result}")
#
# sum (1, 2, 3)
# sum (10, 20, 30)

def i(*numbers):
    result = 0
    for x in numbers:
        result += x
    print(f"i = {result}")

i (5, 10)
i (45, 75)


