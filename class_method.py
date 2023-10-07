class Employee:
    leave = 4
    def __init__(self , name) :
        self.name = name
        
     # class method is a method used to bound the class and not obj of the cls   
    @classmethod
    def change_leave(cls,leaves):
        cls.leave= leaves


    @classmethod
    def from_str(cls,string):
        r = string.split("-")
        return cls(r[0],r[1],r[2])
harrry=Employee("harry")
harrry.change_leave(88)
print(harrry.leave)    

karan = Employee.from_str("karan-480-student")
print(karan.name)        