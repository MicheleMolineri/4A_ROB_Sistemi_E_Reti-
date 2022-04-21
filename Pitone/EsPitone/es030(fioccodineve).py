import turtle
import random
        
screen=turtle.Screen()
fiocco=turtle.Turtle()
screen.bgcolor("black")
fiocco.color("blue")
for i in range(6):
    for i in range(5):
        fiocco.forward(30)
        fiocco.right(25)
        fiocco.forward(50)
        fiocco.backward(50)
        fiocco.left(50)
        fiocco.forward(50)
        fiocco.backward(50)
        fiocco.right(25)
    fiocco.backward(120)     
    fiocco.right(60)


screen.exitonclick()