x = int(raw_input())
sum = 0
for __ in range(x):
	y = raw_input().split(" ")
	sum += (float(y[0])*float(y[1]))
print(sum)