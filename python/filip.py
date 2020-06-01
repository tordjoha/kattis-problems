x = raw_input()
numList = x.split()
ints = list(map(int, numList))
A = ints[0]
B = ints[1]

def reverse(num):
    return int(str(num)[::-1])

revA = reverse(A)
revB = reverse(B)

if revA > revB:
    print revA
else:
    print revB