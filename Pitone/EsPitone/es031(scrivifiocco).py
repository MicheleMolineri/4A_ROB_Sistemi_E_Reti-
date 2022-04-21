leggi=open("./testo.txt","w")


import turtle
import random  
turtle.speed(0)     
screen=turtle.Screen()
fiocco=turtle.Turtle()
screen.bgcolor("black")
fiocco.color("blue")
for i in range(6):
    for i in range(5):
        fiocco.forward(30)
        leggi.write("forward : "+ str(30)+"\n")
        
        fiocco.right(25)
        leggi.write("right : "+ str(25)+"\n")
        
        fiocco.forward(50)
        leggi.write("forward : "+ str(50)+"\n")
        
        fiocco.backward(50)
        leggi.write("backward : "+ str(50)+"\n")
        
        fiocco.left(50)
        leggi.write("left : "+ str(50)+"\n")
        
        fiocco.forward(50)
        leggi.write("forward : "+ str(50)+"\n")
        
        fiocco.backward(50)
        leggi.write("backward : "+ str(50)+"\n")
        
        fiocco.right(25)
        leggi.write("right : "+ str(25)+"\n")

    fiocco.backward(120)  
    leggi.write("forward : "+ str(120)+"\n")   
    fiocco.right(60)
    leggi.write("right : "+ str(60)+"\n")

leggi.close()
screen.exitonclick()
