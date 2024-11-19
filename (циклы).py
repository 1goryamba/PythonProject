number = 1

while number < 5:
    print (f" number = {number}")
    number += 1
    print ("End")

number = 10


number = 10

while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}")
print("End")


message = "testing"

for p in message:
    print (p)

name = "Igor"

for i in name:
    print (i)

for c in range (7):
    print (c, end ="")

for x in range(18, 21):
    print (x, end="")

for n in range (0, 15 , 3):
    print (n, end= "")

message = "hello"
for c in message:
    print (c)
else:
    print (f"test")

i = 5
j = 5
while i < 10:
    while j <10:
        print( i * j, end="\t")
        j += 1
    print ("\n")
    j = 5
    i += 5

for x1 in "a1":
    for x2 in "a2":
        print (f"{x1}{x2}")

number = 0
while number <5:
    number += 1
    if number ==3:
        break
    print (f"number={number}")

number = 0
while number <5:
    number += 1
    if number ==3:
        continue
    print (f"number={number}")