def enigma(x,y,z):
    if x == len(y):
        return(z)
    elif x < len(y):
        return(y[x:])
    else:
        s = foo(z)
        return(s+y)
def foo(w):
    r = ""
    for i in range(len(w)-1,-1,-1):
        r = r + w[i]
    return(r)
	    
one = enigma(7,"caramel","dulce de leche")
two = enigma(3,"cupcake","vanilla")
three = enigma(10,"pie","nomel")

print(one, two, three)