from re import X


def harry():
    x =20
    def raham():
        global x
        x = 19
    print("before calling rohan()",x)
    raham()
    print('after calling rohan()',x)    
    
harry() 
print(x)   