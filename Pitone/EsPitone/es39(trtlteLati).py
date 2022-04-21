import turtle
lati=int(input("inserisci il numero dei lati : "))

linea=turtle.Turtle()
schermo=turtle.Screen()
gradi=(180*(lati-2))/lati
var=gradi-90
for _ in range(lati):
    linea.forward(100)
    linea.right(90-var)

schermo.exitonclick()

