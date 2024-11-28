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