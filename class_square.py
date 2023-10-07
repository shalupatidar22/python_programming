class Calculator:
    def __init__(self,num):
        self.number = num
    
    def square(self):
        print(f"the value of {self.number} square is {self.number**2}")
    
    def cube(self):
        print(f"the value of{self.number} cube is {self.number**3}")
    @staticmethod
    def greet():
       print("good morning")

a = Calculator(5)
a.square()    
a.cube()
a.greet()
        