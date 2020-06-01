numberOfDataSets = int(input())

def sumDigits(n, base):
    total = 0
    while (n > 0):
        remainder = n % base
        total += remainder*remainder
        n = int(n/base)
    return total

for i in range(0, numberOfDataSets):
    dataSet = input().split(" ")
    dataSetNumber = int(dataSet[0])
    dataSetBase = int(dataSet[1])
    dataSetInteger = int(dataSet[2])
    sumOfDigits = sumDigits(dataSetInteger, dataSetBase)
    print('{} {}'.format(dataSetNumber, sumOfDigits))
