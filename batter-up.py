x = int(raw_input())
y = raw_input().split(" ")
numbers = map(float, y)
sumNum = sum(x for x in numbers if x > 0)
numNeg = sum(1 for number in numbers if number < 0)
slug = sumNum/(x-numNeg)
print(slug)