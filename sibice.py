from math import sqrt

x = raw_input()
y = x.split()
N = int(y[0])
W = int(y[1])
H = int(y[2])
a = sqrt(W*W + H*H)

for i in range(N):
	z = int(raw_input())
	if z <= a:
		print("DA")
	else:
		print("NE")
