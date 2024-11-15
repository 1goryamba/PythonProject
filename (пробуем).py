def add(a, b): #функция для сложения двух чисел
    return a + b

import unittest #библиотека

class TestAdd(unittest.TestCase): #создание класса testadd – идущий от unittest.test.case

    def test_add(self): #внутри класса метод test_add – проверка результата функции add
        self.assertEqual(add(2, 3), 5) #Метод assertEqual сравнивает ожидаемый результат с фактическим результатом выполнения функции.

if __name__ == '__main__':
    unittest.main()


def add (a, b):
    return a + b

import unittest

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 3), 6)

if __name__ == '__name__':
    unittest.main()