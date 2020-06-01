x = int(input())
for __ in range(x): #Comparison loops
    firIn = input()
    secIn = input()
    differences = []
    if(len(firIn) == len(secIn)):
        firList = list(firIn)
        secList = list(secIn)
        for i in range(len(firList)):
            #print('is {} equal to {}?'.format(firList[i], secList[i]))
            if (firList[i] == secList[i]):
                differences.append(".")
            else:
                differences.append("*")
    else:
        print("The imputs are not equal in length!")

    output1 = ''.join(firIn)
    output2 = ''.join(secIn)
    output = ''.join(differences)
    print(output1)
    print(output2)
    print(output)
    print()
