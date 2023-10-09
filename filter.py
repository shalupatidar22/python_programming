


list1 = [2,4,5,3,4,5]
def is_greater(num):
    return num<5


greater = list(filter(is_greater,list1))
print(greater)


def common(l1,l2):
    l =[]
    for i in l1:
        if i in l2:
            l.append(i)
        return l  
l1 = [2,3,4,5,6]
l2=[2,5,3,7,8,9]
print(common(l1,l2))     

numbers = [3,5,6,7,8]
def larg(l):
    return max(l) - min(l)
print(larg(numbers))
    
    
matrix= [[1,2,3],[7,8,9],[8,9,7]]
#for sublist in matrix:
#     for i in sublist:
# #      print(i,end=" ,") 
       
print(matrix[1][1])       



number = list(range(1,11))
print(number)
print(number.pop(0))
print(number)
print(number.index(6,4))


def square(s):
    l4=[]
    for i in s:
        l4.append(i**2)
        return l4
    
s = list(range(1,11))
print(square(s))



def countl(list1):
    count = 0
    for i in list1:
        if type(i)==list:
            count +=1
            return count
mixed = [12,[3,4,3],[3,3,4],[3]]
print(countl(mixed))        