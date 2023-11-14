bString = "00011010"
dTotal = 0
bString = bString[::-1]
for i in range(len(bString)):
    power2 = 2**i
    dTotal += int(bString[i])*power2
print(dTotal)
dTotal += 1
newB = ""
while(dTotal > 0):
  newB+= str(dTotal%2)
  dTotal = dTotal//2
print(newB[::-1])