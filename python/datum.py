from datetime import date
x = input().split()

day = int(x[0])
month = int(x[1])
findDate = date(2009, month, day)
if (findDate.weekday() == 0):
    print('Monday')
elif (findDate.weekday() == 1):
    print('Tuesday')
elif (findDate.weekday() == 2):
    print('Wednesday')
elif (findDate.weekday() == 3):
    print('Thursday')
elif (findDate.weekday() == 4):
    print('Friday')
elif (findDate.weekday() == 5):
    print('Saturday')
elif (findDate.weekday() == 6):
    print('Sunday')
