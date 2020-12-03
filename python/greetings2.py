x = input()
letterList = list(x)
eCount = 0
for i in letterList:
    if i == 'e':
        eCount += 1
letterList.remove('y')
letterList.append('e'*eCount)
letterList.append('y')
print("".join(letterList))