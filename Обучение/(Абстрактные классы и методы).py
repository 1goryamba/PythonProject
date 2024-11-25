import abc
class Shape(abc.ABC):
    @abc.abstractmethod
    def area (self): pass

class Rectangle(Shape):
    def __init__(self, width, high):
        self.width = width
        self.high = high
    def area(self): return self.width + self.high

rect = Rectangle(150,920)
print("Rectangle area:", rect.area())   