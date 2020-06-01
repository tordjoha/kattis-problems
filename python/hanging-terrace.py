tMax, e = map(int, raw_input().split(" "))
curr = 0
deniedGroups = 0
for __ in range(e):
	gAction, gCount = raw_input().split(" ")
	gCount = int(gCount)
	if gAction == 'enter':
		if (curr + gCount) <= tMax:
			curr += gCount
		else:
			deniedGroups += 1
	else:
		curr -= gCount
print(deniedGroups)
