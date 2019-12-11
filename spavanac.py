from datetime import timedelta
x = input().split()
inTime = timedelta(hours = int(x[0]), minutes = int(x[1]))
alarmTime = timedelta(hours = 0, minutes = 45)
beforeInput = inTime - alarmTime
print('{} {}'.format(int(beforeInput.seconds/3600), (beforeInput.seconds//60)%60))
