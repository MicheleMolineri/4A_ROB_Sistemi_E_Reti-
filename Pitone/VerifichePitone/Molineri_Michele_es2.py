#Crea un programma Python che disegni una griglia 4 x 4
# a maglie quadrate di lato 10, come quella a fianco, 
# mediante il modulo turtle. Utilizza il minor numero 
# di righe di codice.

import turtle
turtle.speed(0) 
tart=turtle.Turtle()
screen=turtle.Screen()

def quadrato(x,y):
    tart.goto(x,y)#sposto la prima linea nelle coordinate
    for _ in range(4): #4 volte 4 lati
        tart.right(90) #ruota 
        tart.forward(10)#va avanti
    tart.forward(10)

x,y=0,0

for _ in range(4):
    for _ in range(4):
        quadrato(x,y)
        x+=10   #creo la righe della griglia
    x-=40
    y-=10 # faccio le righe 4 volte e creo la griglia

screen.exitonclick()
    
