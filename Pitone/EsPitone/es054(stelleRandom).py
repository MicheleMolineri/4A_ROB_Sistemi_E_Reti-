"""
Scrivere un programma in Python nel quale utilizzando il modulo turtle:
- sia presente una funzione che disegni una stella nelle coordinate x e y (passate come parametri alla funzione) 
- disegni 50 stelle sullo screen posizionate in posizioni casuali.
"""

import turtle
import random


LUNGH,GRAD=15,144

def disegnaStella(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
   
    for _ in range(5):
        turtle.forward(LUNGH)
        turtle.right(GRAD)

screen=turtle.Screen()
turtle.Turtle()
turtle.speed(0)
turtle.color("yellow")
screen.bgcolor("black")



for _ in range(50):
    x,y=random.randint(-300,300),random.randint(-300,300)
    disegnaStella(x,y)

turtle.exitonclick()
