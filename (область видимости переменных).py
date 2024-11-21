# # глобальный контекст

# name = "Igor"
#
# def hi():
#     print("Hello", name)
#
# def bye():
#     print("Bye", name)
#
# hi()
# bye()

# локальный контекст

# def hi():
#     name = "Igor"
#     print("Hi", name)
#
# def bye():
#     name = "Igor"
#     print("Bye", name)
#
# hi()
# bye()

# def outer():
#     n = 5
#
#     def inner():
#         print(n)
#
#     inner()
#     print(n)
#
# outer()


# def outer():
#     n = 5
#
#     def inner():
#         n = 25
#         print(n)
#     inner()
#     print(n)
#
# outer()


def outer():
    n = 5

    def inner():
        nonlocal n
        n = 25
        print (n)
    inner()
    print(n)

outer()

