import random
n=random.randint(1,100)
guess=1
for i in range(100):
    print('guess number')
    number=int(input('enter number betweem 1 to 100'))
    guess+=1
    if n<number:
        print(f'too high {number}')
    elif n>number:
        print(f'llow {number}')
    else:
        print(f"you guess the number right in {guess} times and th number is {number}")  
        break      