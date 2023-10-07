class Employee:
    company='google'    # class attribute which is valid for all instance 

r=Employee()
s=Employee()
r.company='youtube'   #object attribute
# when we have onject attribute then the program priortise the obj attribute 
print(r.company)    
print(s.company)
r.salary=900       #we can make instant attribute of object
print(r.salary)