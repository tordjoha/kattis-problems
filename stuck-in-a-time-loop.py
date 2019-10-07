inNum = input()
i = 1
if str(inNum).isdigit() and 1 <= inNum <= 100:
    for x in range (0, inNum):
        print (str(i) + " Abracadabra")
        i += 1  
else:
    print("Input is not a number or not in range")