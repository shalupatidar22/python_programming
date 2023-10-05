def splie(arr,n,k):
    for i in range(0,k):
        x = arr[0]
        for j in range(0,n-1):
            arr[j] = arr[j+1]
        arr[n-1] = x
arr  = [12,10,5,6,55,66]
n = len(arr)
position  = 2
splie(arr,n,position) 
for i in range(0,n):
    print(arr[i],end = ' ',)       
    
    
def largest(a,b):
    if a>b:
        return a
    else:
        return b
a =10
b =45
print(largest(a,b) )  

