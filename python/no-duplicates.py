x = input().split()
wordList = [] #unique words
allList = [] #all words

for i in x:
    if i not in wordList:
        wordList.append(i)

for j in x:
    allList.append(j)

if len(wordList) == len(allList):
    print('yes')
else:
    print('no')
