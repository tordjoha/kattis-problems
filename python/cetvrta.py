points = []
x = []
y = []

for __ in range(0, 3):
    points.append(list(input().split()))

for i in points:
    x.append(i[0])
    y.append(i[1])

points = [0, 0]

for i in range(0, 3):
    if x.count(x[i]) == 1:
        points[0] = x[i]
    if y.count(y[i]) == 1:
        points[1] = y[i]

print('{} {}'.format(points[0], points[1]))
