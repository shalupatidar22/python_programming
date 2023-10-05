class phone:
    def __init__(self,brand,model,price):
        self.brand= brand
        self.model = model
        self._price = price
        
    def make_a_call(self,phone):
        print(f"calling {phone}...") 
     
    def full_name(self):
        return f"{self.brand} {self.model}"    
           
           
l = [4,3,5] 
l.sort()
print(l)    
phone1 =phone("npkia",1000,9994)
print(phone1._price)

from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle(shape):
    type = "Rectangle"
    sides  = 4
    def __init__(self):
        self.length=6
        self.breadth  = 7
        
        
    def printarea(self):
        return self.length*self.breadth
    
rec1 = Rectangle()
print(rec1.printarea())    
        