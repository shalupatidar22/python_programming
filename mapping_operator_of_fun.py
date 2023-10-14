class Employee:
    leave = 3
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role= role
        
    def printdetails(self):
        return f"the name is {self.name} and salary is {self.salary} "       
    
    @classmethod
    def change_leave(cls,newleave):
        cls.change_leave = newleave
        
        
    def __add__(self,other):
        return self.salary +other.salary
    
    
    def __truediv__(self,other):
        return self.salary / other.salary
    
    def __str__(self):
        return f"Employee {self.name} and the salary of employee is  {self.salary}  and his role is  {self.role}"
    
enp =Employee("hary",889,"programmer")
emp = Employee("rohan",88,"cleaner")    
print(enp+emp)   
print(enp/emp)
print(str(enp))

 