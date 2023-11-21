#!/usr/bin/env python3

bString = "0011101"
dTotal = 0
#bString = bString[::-1]
lsd_idx = len(bString)-1
for i in range(lsd_idx,-1,-1):
    power2 = 2**i
    dTotal += int(bString[lsd_idx-i])*power2
print(dTotal)
dTotal += 1
newB = ""
while(dTotal > 0):
  newB+= str(dTotal%2)
  dTotal = dTotal//2
print(newB[::-1])