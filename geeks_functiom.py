def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True
num=is_prime(23)
print(num)  

#program of defualt function : which takes default argument
def default(name,myname='shalu'):
    print(f'your name is {name} and my name is {myname}')   
n=default('tanisha')
print(n)



# argument function: we can print each element in string using *arg function
def myarg(*arga):
    for arg in arga:
        print(arg)
myarg('shalu' , 'is','not','focused')  


    # **kwargs fun can print both the key and value in desirable format
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))  #format of printing the key and value
 
 
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')      