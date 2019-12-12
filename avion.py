firstIn = input()
secondIn = input()
thirdIn = input()
fourthIn = input()
fifthIn = input()
x = []
if ("FBI" in firstIn):
    x.append(1)
if ("FBI" in secondIn):
    x.append(2)
if ("FBI" in thirdIn):
    x.append(3)
if ("FBI" in fourthIn):
    x.append(4)
if ("FBI" in fifthIn):
    x.append(5)
if (len(x) == 0):
    print("HE GOT AWAY!")
if (len(x)) > 0:
    print(*x, sep=" ")
