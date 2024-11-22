class Counter:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Counter(self.value + other.value)


counter1 = Counter(5)
counter2 = Counter(15)
counter3 = counter1 + counter2
print(counter3.value)

class Test:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Test(self.value + other.value)


Test1 = Test(50)
Test2 = Test(30)
Test3 = Test1 + Test2
print(Test3.value)

class Counter:
    def __init__(self, value):
            self.value = value

    def __add__(self, other):
        return self.value + other

counter1 = Counter(10)
result = counter1 + 25
print (result)

class Counter:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return self.value > 0

def test(counter):
    if counter:print("Counter= True")
    else: print("Counter = False")

counter1 = Counter(3)
test(counter1)

counter2 = Counter(-10)
test(counter2)

class Counter:
    def __init__(self, value):
        self.value = value
    def __bool__(self):
        return self.value > 0

counter1 = Counter(20)

while(counter1):
    print("counter1: ", counter1.value)
    counter1.value -=5

