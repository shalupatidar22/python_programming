class shalu:
    def __init__(self,age,ability,dream,success):
        self.age = age
        self.ability = ability
        self.dream = dream
        self.success = success
class lalu(shalu):
    def bhai(self):
        return f"she is my sister and her age is {self.age} and has a ability of {self.ability} her is to become {self.dream} and she is successfull in {self.success}"
    
    @staticmethod
    def greet():
         print("hello shalu")
    
    
shalu1 = shalu(19,"good","data scientist","engineer")
lalu1 = lalu(20,"exll","bca","ca")
print(shalu1.age)
print(lalu1.age,lalu1.ability)


lalu1.greet()
hh  = lalu.bhai(shalu1)
print(hh)                 