x = input().split()
numHands = int(x[0])
domSuit = x[1]
cards = numHands*4
sum = 0
for i in range(cards):
    y = input()
    firstChar = y[:-1]
    secondChar = y[-1:]
    if (firstChar == "A"):
        sum += 11
    elif (firstChar == "K"):
        sum += 4
    elif (firstChar == "Q"):
        sum += 3
    elif (firstChar == "J"):
        if (secondChar == domSuit):
            sum += 20
        else:
            sum += 2
    elif (firstChar == "T"):
        sum += 10
    elif (firstChar == "9"):
        if (secondChar == domSuit):
            sum += 14
        else:
            sum += 0
    elif (firstChar == "8"):
        sum += 0
    elif (firstChar == "7"):
        sum += 0
print(sum)
