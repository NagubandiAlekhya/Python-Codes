#abstraction
'''
from abc import ABC,abstractmethod
class Area(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Square(Area):
    def calculate_area(self):
        
        print("in square method")
class Rectangle(Area):
    pass
obj=Square()
obj.calculate_area()

'''
#abstraction
from abc import ABC,abstractmethod
class Area(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_circular_area(self):
        pass
class Square(Area):
    def calculate_area(self):
        print("in square method")
    def calculate_circular_area(self):
        pass
class Rectangle(Area):
    pass
obj=Square()
obj.calculate_area()

