#single inheritance
class Employee:
    company='google'
    
    def getsalary(self):
        print('i am getting 1000 salary')
        
class Programer(Employee):
    def getdetails(self):
        print('details are there.....')
                
e=Employee()
p=Programer()
p.getsalary()
e.getsalary()
p.getdetails()        


#multiple inheritance
class person:
    name='ravi'
    
    def Takebreath(self):
        print('i am breathimg.....')
        
    def Eating(self):
        print('i love eating')

class Student:
    college='oct'
    
    def  details(self):
        print('i am  a student')
   
class worker(person ,Student):
    pass

h=person()
s=Student()
w=worker()
w.Eating()
w.details()
w.Takebreath()



#multilevel inheritance
v=lambda x:x*2
print(v(4))     

s=lambda a,b: a if a>b else b
print(s(3,7))           