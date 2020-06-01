#NOT FINISHED
#Cryptographer's Conundrum
#KATTIS

x = raw_input()
l = list(x)
alreadyThere = 0
for i in range(len(l)):
	print(l[i])
	if (l[i] == "P") or (l[i] == "E") or (l[i] == "R"):
		alreadyThere += 1
		print("+1")
	else:
		alreadyThere += 0
print(alreadyThere)
print(len(l)-alreadyThere)