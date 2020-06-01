import math
x = int(raw_input())
sum = 0
for __ in range(x):
	y = int(raw_input())
	powI = int(str(y)[-1:])
	number = int(str(y)[:-1])
	sum += math.pow(number, powI)
print(str(int(sum)))