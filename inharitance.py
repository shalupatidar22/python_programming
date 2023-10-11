class son:
    bascketball = 9
    
    
class dad:
    dance = 4
   
    def intee(self):
        
        return f"this is my hobby {self.dance}"    
    
class granson(dad,son):
    
    def ooo(self):
        
        return f"the is my ohassion{self.bascketball}"   
    
    
fatyy = son()
saddy = dad()
maddy = granson()   
print(maddy.bascketball)
print(maddy.dance)

class Employee:
    company = "google"
    def detail(self):
        return f"i am working in this company {self.company}"

class HR(Employee):
    work = "software engineer"
    def mydetails(self):
        return f"i am working in the post of {self.work}"
    
class worker(Employee):
    age = 32
    def quality(self):
        return f" my age is {self.age}"
class member(HR):
    name = "harry"
    def membr(self):
        return f"i am the memeber  of hr {self.name}"
    
aman = Employee()
chaman = HR()
daman = worker()
karan = member()                    
print(daman.company)
print(karan.work)