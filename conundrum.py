userInput = input().upper()
chunkNum = len(userInput) / 3
days = 0
chunks = [userInput[i:i+3] for i in range(0, len(userInput), 3)]
for x in range(0, int(chunkNum)):
    if chunks[x][0] != "P":
        days += 1
    if chunks[x][1] != "E":
        days += 1
    if chunks[x][2] != "R":
        days += 1
    else:
        days = 0
print(days)