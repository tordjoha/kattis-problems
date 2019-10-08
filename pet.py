c1 = raw_input().split()
c2 = raw_input().split()
c3 = raw_input().split()
c4 = raw_input().split()
c5 = raw_input().split()

def summing(x):
	total = 0
	for i in range(len(x)):
		total += int(x[i])
	return total

r1 = summing(c1) 
r2 = summing(c2) 
r3 = summing(c3) 
r4 = summing(c4)
r5 = summing(c5) 

winner = max(r1, r2, r3, r4, r5)
if winner == r1:
	print("1 " + str(r1))
elif winner == r2:
	print("2 " + str(r2))
elif winner == r3:
	print("3 " + str(r3))
elif winner == r4:
	print("4 " + str(r4))
elif winner == r5:
	print("5 " + str(r5))

#IMPROVEMENTS
#-for loop to push c1-c5 to array
# and use function on it
