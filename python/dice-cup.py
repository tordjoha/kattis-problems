numOfFaces = raw_input().split()
d1 = int(numOfFaces[0])
d2 = int(numOfFaces[1])

if( d2 < d1):
	d3 = d1
	d1 = d2
	d2 = d3

i = (d1 + 1)
while (i < (d2+2)):
	print(i)
	i += 1
