userInput = input()
wordLength = int(len(list(userInput))/3)

firstWord = userInput[:wordLength]
secondWord = userInput[wordLength:-wordLength]
thirdWord = userInput[-wordLength:]
finalWord = ""

if( firstWord == secondWord):
    finalWord = firstWord
if (firstWord == thirdWord):
    finalWord = firstWord
if (secondWord == thirdWord):
    finalWord = secondWord

print(finalWord)
