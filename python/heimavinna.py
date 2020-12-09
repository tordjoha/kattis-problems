x = input().split(';')

tasksToSolve = 0
for i in x:
    if i.__contains__('-'):
        splitDigits = i.split('-')
        taskCount = (int(splitDigits[1])-int(splitDigits[0])) + 1
        tasksToSolve += taskCount
    else:
        tasksToSolve += 1

print(tasksToSolve)