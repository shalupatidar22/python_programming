class Employee:
    leaves = 8
    
    def __init__(self,name,salary,arole):
        self.name= name
        self.salary = salary
        self.arole = arole
        
    def printdetails(self):
        return f"the name is {self.name} salary is {self.salary} and role is {self.arole}" 
    
    @classmethod
    def change_leave(cls,newleave):
        cls.leaves = newleave
        
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    
    @staticmethod
    def printgood(string):
        print("this is good"+ " " +string)
        
    
haryy = Employee("harry ", 255,"entercity")   
rohan = Employee("rohan", 677,"student")
karan = Employee.from_dash("karan-480-student")
karan.leaves = 56   
print(karan.salary)  
print(karan.leaves)   
karan.printgood("harry")