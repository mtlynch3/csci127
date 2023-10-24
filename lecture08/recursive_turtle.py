
import turtle
def setUp(t, dist, col):
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)

def nestedTriangle(t, side):
    if side <= 10: #base case, side length is too small
        return #do nothing, ends recursive call
    #otherwise keep going, draw a triangle
    for i in range(3):
           t.forward(side)
           t.left(120)
    #call function again but with the side length halved
    nestedTriangle(t, side/2)

def fractalTriangle(t, side):
   if side > 10:
       for i in range(3):
           t.forward(side)
           t.left(120)
           fractalTriangle(t, side/2)

def main():
    wn = turtle.Screen()
    side = int(input("Enter side of a triangle: "))
    nancy = turtle.Turtle()
    setUp(nancy, 100, "orchid")
    nestedTriangle(nancy, side)

    frank = turtle.Turtle()
    frank.speed(10)
    setUp(frank, -100, "orangered")
    fractalTriangle(frank, side)
    wn.exitonclick()

if __name__ == "__main__":
     main()