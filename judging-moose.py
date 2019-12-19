x = input().split(" ")
L = int(x[0])
R = int(x[1])

sum = 0

if (L == R and L != 0 and R != 0):
    sum = (L + R)
    print('Even {}'.format(sum))

elif (L == 0 and R == 0):
    print("Not a moose")

elif (L != R):
    if (L > R):
        sum = L*2
    elif (R > L):
        sum = R*2
    print('Odd {}'.format(sum))
