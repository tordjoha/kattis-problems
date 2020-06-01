input = raw_input()
x = input[0]
for char in input[1:]:
	if char != x[-1]:
		x += char
print(x)
