costOfSeed = float(raw_input())
numLawns = int(raw_input())

totalCost = 0
for i in range(0,numLawns):
	x = raw_input().split()
	width = float(x[0])
	length = float(x[1])
	totalCost += (width * length) * costOfSeed
	
print("%.7f" %totalCost)