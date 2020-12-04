numOfDatasets = int(input())
for x in range(numOfDatasets):
    dataSet = input().split()
    days = int(dataSet[1])
    candles = int(((days * (days + 1) / 2) + days))
    print(str(x + 1) + " " + str(candles))