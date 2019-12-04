from collections import Counter

hand = input().split(" ")
sList = []
for card in hand:
    sList.append(card[:1])
counts = (Counter(sList))

print(max(counts.values()))
