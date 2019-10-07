mPerMonth = int(raw_input())
months = int(raw_input())
totalMB = 0
i = 0
while i < months:
    totalMB += mPerMonth    
    thisMonthMB = int(raw_input())
    totalMB -= thisMonthMB
    i += 1
totalMB += mPerMonth
print(totalMB)