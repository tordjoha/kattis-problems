x = int(raw_input())
y = raw_input().split(" ")
lessThenZero = 0
for i in range(x):
	if int(y[i]) < 0:
		lessThenZero += 1
	else:
		lessThenZero += 0
print(lessThenZero)