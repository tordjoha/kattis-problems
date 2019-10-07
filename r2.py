x = raw_input()
nums = x.split()
ints = list(map(int, nums))
R1 = ints[0]
S = ints[1]
y = S*2
R2 = y-R1
print(R2)