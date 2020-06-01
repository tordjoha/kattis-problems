x = raw_input()
numArr = x.split()
ints = list(map(int, numArr))
X = ints[0]
Y = ints[1]
N = ints[2]

i = 1
while (i <= N):
    if i % X == 0 and i % Y == 0:
        print("FizzBuzz")
    elif i % X == 0:
        print("Fizz")
    elif i % Y == 0:
        print("Buzz")
    else:
        print (i)
    i += 1