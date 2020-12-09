cases = int(input())
for i in range(cases):
    sentence = input().split(" ")
    if sentence[0] == 'Simon' and sentence[1] == 'says':
        for item in sentence[2:]:
            print(item, end=' ')