# def outer():
#     n = 5
#
#     def inner():
#         nonlocal n
#         n += 1
#         print (n)
#
#     return inner
#
# fn = outer()
#
# fn()
# fn()
# fn()

# def test():
#     n = 15
#
#     def test1():
#         nonlocal n
#         n += 1
#         print (n)
#
#     return  test1
#
# xn = test()
#
# xn()
# xn()
# xn()

# def multiply(n):
#     def inner(m): return n * m
#
#     return inner
#
# fn = multiply(5)
#
# print(fn(5))
# print(fn(6))
# print(fn(7))

# def test(a):
#     def testing(b): return a * b
#
#     return testing
#
# xn = test(5)
#
# print (xn(5))
# print (xn(6))
# print (xn(7))

def multiply(n): return lambda m: m * n

fn = multiply(5)

print(fn(5))
print(fn(6))
print(fn(7))