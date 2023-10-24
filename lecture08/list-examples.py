
def add2(num):
    #modify num; data type is number (int/float)
    num = num + 2
    return num
def swap(inList):
    #modify inList; data type is list
    inList[0], inList[-1] = inList[-1], inList[0]
    return inList

inList1 = [1,2,3,4]
inList2 = swap(inList1)
print(inList1, inList2)

x = 5
y = add2(x)
print(x,y)

