x = raw_input()
splitInput = x.split("-")
y = []
i = 0
while i < len(splitInput):
    y.append(splitInput[i][0])
    i += 1
z = ''.join(y)
print(z)