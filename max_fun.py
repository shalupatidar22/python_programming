


def maximum(num1, num2, num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3  
          
          
m = maximum(2,5,6,) 
print("the value of the maximum is" + str(m))         


# write a python program using function to convert celsius to fahrenhut



def farh(cel):
    return (cel *(9/5)) +32


c = 45
f = farh(c)
print("fahreheit temperature is" + str(f))


# how do you prevent a python print () funtion to print a new line at the end

print("hellow" , end=" ")
print("how " , end=" ")
print("are" , end=" ")
print("you", end=" ")

#write a recursive fun to calculate the sum of first n natural numbers
def sum_recursive(n):
    if n == 1 or n==0:
        return 1
    return sum_recursive(n-1)+n

s = sum_recursive(6)
print(s)


#writw a fun to print first n lines of the following pattern:
# * * *
# * *
# *

n =6
for i in range(n):
    print("*" * (n-i))
    
# write a python program which convert inches to cms

def cm(inch):
    return (inch* (1/12))

c = cm(5)
print(c)        


#write a python program to remove a given word from a string and strip it at the same time
this = "    harry is a good      "
print(this)
print(this.strip())


def remove_and_split(string , word):
    newstr=string.replace(word , "")
    return newstr.strip()

this = "     harry is  a goos     "     #strip remove white space 
n = remove_and_split(this , "harry")
print(n)


# write a python program to print  multiplication table of a given num
num = int(input("enter the num"))
for i in range(1, 11):
    print(f"{num}X{i}= {num*i}")    