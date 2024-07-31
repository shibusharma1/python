from abc import ABC, abstractmethod

class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(AbstractShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Creating an instance of Rectangle
rect = Rectangle(4, 5)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")

# Trying to instantiate AbstractShape directly will raise an error
# shape = AbstractShape()
