from collections import Counter

x = raw_input().split(" ")
h1 = x[0]
h2 = x[1]
h3 = x[2]
h4 = x[3]
h5 = x[4]

h1 = h1[-1:]
h2 = h2[-1:]
h3 = h3[-1:]
h4 = h4[-1:]
h5 = h5[-1:]

array = [h1, h2, h3, h4, h5]
handStrength = (Counter(array).keys())
print(len(handStrength))