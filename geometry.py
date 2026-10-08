from abc import ABC, abstractmethod
from math import pi

class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass
    
    @abstractmethod
    def perimetter(self):
        pass
    
    def __repr__(self):
        return f"aire = {self.aire():.2f}, perimetter = {self.perimetter():.2f}"
    
    
class Rectangle(Forme):
    def __init__(self, long: int, larg: int):
        self.long = long
        self.larg = larg
    
    def aire(self):
        return self.long*self.larg
    
    def perimetter(self):
        return 2*(self.long+self.larg)

class Circle(Forme):
    def __init__(self, radius: int):
        self.radius = radius
    
    def aire(self):
        return pi*self.radius**2
    
    def perimetter(self):
        return 2*pi*self.radius

class Squart(Forme):
    def __init__(self, side: int):
        self.side = side
    
    def aire(self):
        return self.side*self.side
    
    def perimetter(self):
        return 4*self.side

if __name__ == '__main__':
    rec = Rectangle(5, 3)
    circ = Circle(4)
    sqrt = Squart(6)
    for el in [rec, circ, sqrt]:
        print(el)