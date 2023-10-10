import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=time.strftime('%H')
print(timestamp)
timestamp=time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)






t=time.strftime('%H:%M:%S')
hour=time.strftime('%H')
hour=int(input('enter the time:'))
print(hour)

if (hour<12):
    print('good morning')
elif (hour>12 and hour<17):
    print('good afternoon')
elif (hour>=17 and hour<=19):
    print('good evening')
else:
    print('good nigth')            