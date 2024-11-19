
language = "ru" # правда – выводим (if)
if language == "ru":
    print("test")


language = "ru" # неправда – не выводим (if)
if language == "eng":
    print("test")

language = "ru"
if language == "eng": # неправда, не выводим (if)
    print ("test")
else: # если неправда то выведем значение
    print ("test 555")

language = "ru"
if language == "eng":
    print ("hi")
    print ("h8")
else: # если неправда то выводим значение. Если выражение правда выводим данные из первой конструкции
    print ("t2")
    print ("t5")

language = "ru"
if language == "eng":
    print ("c8")
    print ("c9")
elif language == "ru":
    print ("cb1")
    print ("cb2")
else:
    print ("tgg")
    print ("t88")


language = "ru"
if language == "eng":
    print ("123")
elif language == "ru":
    print ("321")
elif language == "eu":
    print ("111")
else:
    print("priv")


language = "eng"
daytime = "morning"
if language == "eng":
    print("test1")
    if daytime == "morning":
        print("test5")
    else:
        print("hi")

language = "ru"
daytime = "morning"
if language == "ru":
    print("hi")
if daytime == "morning":
    print("hi 5")
else:
     print("hi 10")