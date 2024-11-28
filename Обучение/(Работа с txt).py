myfile = open("testing.txt", "w")

myfile.close()

try:
    myfile = open("testing.txt", "w")
    try:
        print("Работа с файлом")
    finally:
        myfile.close()
except Exception as ex:
    print(ex)

with open("testing.txt", "w") as myfile:
    print("Работа с файлом myfile")

with open("testing.txt", "w") as file:
    file.write("hello world")

print("Файл записан")

with open("testing.txt", "a") as file:
    file.write("\nhello work")

print("Файл изменен")

lines = ["Hello Word\n", "Hello Work\n", "Hello World\n"]
with open("testing.txt", "a") as file:
    file.writelines(lines)

print("Список строк записан в файл")


with open("hello.txt", "a") as myfile:
    print("\nhello metanit.com", file=myfile)

with open("testing.txt", "a") as myfile:
    print("\nhello testing.com", file=myfile)