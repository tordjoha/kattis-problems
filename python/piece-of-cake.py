x = raw_input().split(" ")
n = int(x[0])
h = int(x[1])
v = int(x[2])

cakeUpLeft = h * v * 4
cakeUpRight = ((n - v) * h) * 4
cakeDownLeft = ((n - h) * v) * 4
cakeDownRight = ((n - v) * (n - h)) * 4

cakeSlices = [cakeUpLeft, cakeUpRight, cakeDownLeft, cakeDownRight]

print(max(cakeSlices))