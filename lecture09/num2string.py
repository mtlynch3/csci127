#LECTURE SLIP PROBLEM 1

def prob4(amy, beth):
  if amy > 4:
    print("Easy case")
    kate = -1
  else:
    print("Complex case")
    kate = helper(amy, beth)
  return (kate)

def helper(meg, jo):
  s = ""
  for j in range(meg):
    print(j, ":", jo[j])
    if j % 2 == 0:
      s = s + jo[j]
      print("Building s:", s)
  return s

r = prob4(4, "city")
print("Return r: ", r)
r = prob4(2, "university")
print("Return r: ", r)

#LECTURE SLIP PROBlEM 2
def num2string(num):
  numString = ""
  return numString
