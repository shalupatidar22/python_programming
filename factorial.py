num = int(input("enter the num"))
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i
    print(f"the factorial of {num} is {factorial}")