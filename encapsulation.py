
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def printdetails(self):
        return f"this is name {self.name} and salary is {self.salary}"


class Programmer(Employee) :
    def printprog(self):
        return f"the programmer is {self.name} salary is {self.salary}"   
harry = Employee("harry ",233)   
karan= Programmer("karan ",555)
print(karan.printdetails())     