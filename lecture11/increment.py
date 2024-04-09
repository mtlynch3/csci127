def addOne(bString):
  dTotal = 0
  #reverse the input so that we start reading 
  #at the least significant digit (last char in string)
  bString = bString[::-1]
  #generate the powers of two for the place values
  #and multiply that by each digit in the input
  for i in range(len(bString)):
      power2 = 2**i
      dTotal += int(bString[i])*power2
  #increment
  dTotal += 1
  #convert from decimal to binary
  newB = "" #will store our result
  while(dTotal > 0):
    newB += str(dTotal%2)
    dTotal = dTotal//2
  #reverse the string because we started from LSD
  return(newB[::-1])


#UNIT TESTS

if addOne("1001") == "1010":
  print("PASS")
else:
  print("FAIL")

if addOne("1010") == "1011":
  print("PASS")
else:
  print("FAIL")

if addOne("1011") == "1100":
  print("PASS")
else:
  print("FAIL")

if addOne("1100") == "1101":
  print("PASS")
else:
  print("FAIL")