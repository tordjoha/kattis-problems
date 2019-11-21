x = int(raw_input())

def reversedBinaryNumbers(number):
	intToBin = bin(number).replace("0b", "")
	binRev = intToBin[::-1]
	binToInt = int(binRev, 2)
	return binToInt

print(reversedBinaryNumbers(x))