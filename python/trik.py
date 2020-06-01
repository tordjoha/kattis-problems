x = raw_input()
moveList = list(x)
cups = [1, 0, 0]

for i in range(len(moveList)):
	if moveList[i] == "A":
		if cups[0] == 1:
			cups[0] = 0
			cups[1] = 1
		elif cups[1] == 1:
			cups[1] = 0
			cups[0] = 1
	elif moveList[i] == "B":
		if cups[1] == 1:
			cups[1] = 0
			cups[2] = 1
		elif cups[2] == 1:
			cups[2] = 0
			cups[1] = 1
	else:# C
		if cups[0] == 1:
			cups[0] = 0
			cups[2] = 1
		elif cups[2] == 1:
			cups[2] = 0
			cups[0] = 1
		
if cups[0] == 1:
	print(1)
elif cups[1] == 1:
	print(2)
else:
	print(3)
