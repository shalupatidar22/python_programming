class Employee:
    # __init__ is a constructor which is first run as soon as object is created without initialzing it 
    def __init__(self,name,salary,submit) :
        self.name=name
        self.salary=salary
        self.submit=submit
        print('employee is created!')
       # print(f'{self.name} {self.salary}  {self.submit}')
        
    def getdetails(self):
        print(f'the name of the employee is {self.name} and his salary is {self.salary}  and he submit the {self.submit}')    
        
f=Employee('guvi',1000,'sunday') # here the obj is created and init is run
f.getdetails()        