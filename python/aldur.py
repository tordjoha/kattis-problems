friends = int(input())
ageList = []
for age in range(friends):
    fage = int(input())
    ageList.append(fage)
ageList.sort()
print(ageList[0])
