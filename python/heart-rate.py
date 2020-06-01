x = int(input())

for __ in range(x):
    y = input().split()
    b = float(y[0])
    p = float(y[1])

    calcABPM = (60 * b) / p
    minABPM = calcABPM - (60 / p)
    maxABPM = calcABPM + (60 / p)
    print(format(minABPM, '.4f') + " " + format(calcABPM, '.4f') + " " + format(maxABPM, '.4f'))
