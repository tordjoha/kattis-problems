hand = map(str, input().split(" "))
sList = []
for card in hand:
    x = card[0]
    s = 1
    for card2 in hand:
        if x == card2[0]:
            s += 1
    sList.append(s)

print(max(sList))
