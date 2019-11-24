import math
x = int(raw_input())

for __ in range(x):
	nInp = int(raw_input())
	nFact = math.factorial(nInp)
	nFactStr = str(nFact)
	n = nFactStr[-1]
	print(n)
