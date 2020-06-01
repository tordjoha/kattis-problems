import sys
import math

x = int(input())

for __ in range(x):
    y = input().split()
    velocity = float(y[0])
    angle = float(y[1])
    distToWall = float(y[2])
    hLower = float(y[3])
    hUpper = float(y[4])

    hLower += 1
    hUpper -= 1

    angle = math.radians(angle)
    t = distToWall / (velocity * math.cos(angle))
    maths = (velocity * t * math.sin(angle)) - (0.5 * 9.81 * (t**2))

    if (maths < hUpper) and (maths > hLower):
        print('Safe')
    else:
        print('Not Safe')
