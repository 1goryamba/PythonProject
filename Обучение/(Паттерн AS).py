def print_person(person):
    match person:
        case "i1" | "i2" | "i3" as name:
            print(f"Name:{name}")
        case _:
            print("Undefined")

print_person("i1")
print_person("i2")
print_person("i3")

def print_person(person):
    match person:
        case ("i1" | "i2" as name, 18 | 21 as age):
            print(f"i1| name:{name} age: {age}")
        case ("i2" | "i3", 22 | 23) as i2:
            print(f"i2| Name: {i2[0]}  Age: {i2[1]}")
        case _:
            print("Undefined")


print_person(("i1", 21))
print_person(("i3", 22))

