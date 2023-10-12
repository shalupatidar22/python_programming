# we can pass function into a function and to make it in a line we use lambda function 
#lambda function is known as anonynmous function in python 

def fun(fx,value):
    return 6+fx(value)
print(fun(lambda x:x*x , 4))    #we used labda fun as a fun