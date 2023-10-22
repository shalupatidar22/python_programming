class Programer:
    company='microsoft'
    
    def getdetails(self):
        print(f'the programer {self.name} is working in the {self.company}')
        
    @staticmethod
    def greet():
        print('heloo sir ,')   
yup=Programer()
cup=Programer()
yup.name='yarry'        
yup.getdetails()
cup.name='charry'
cup.getdetails()
yup.salary=1000
yup.greet()



#class calculator finding square ,cube and squareroot
class calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f'the square of {self.num} is {self.num**2}')
    
    def cube(self):
        print(f'the cube the {self.num} is {self.num**3}')   
        
    def squareroot(self):
        print(f'the squaroot of {self.num} is {self.num*1/2}') 
        
ans=calculator(5)
# ans.a=4
ans.square() 
ans.cube()
ans.squareroot()           

#class train which can book a ticket

class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    
    def getStatus(self):
        print(f'the name of the train is {self.name} ')
        print(f'the no of seats available in this train is {self.seats}')
        print(f'the price of the ticket is {self.fare}')
        
    def bookTicket(self):
        if(self.seats>0):
            print(f'your ticket is booked and your seat is {self.seats}')
            self.seats -=self.seats
        else:
            print('sorry the train is full')    
     
intercity=Train('intercity express' , 90,300)        
intercity.getStatus()
intercity.bookTicket()