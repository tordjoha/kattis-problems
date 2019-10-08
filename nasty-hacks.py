n = int(raw_input())

for i in range(0, n):
	x = raw_input().split()
	r = int(x[0])
	e = int(x[1])
	c = int(x[2])

	if ((e - c) > r):
		print("advertise")
	elif ((e - c) == r):
		print("does not matter")
	elif ((e - c) < r):
		print("do not advertise")
