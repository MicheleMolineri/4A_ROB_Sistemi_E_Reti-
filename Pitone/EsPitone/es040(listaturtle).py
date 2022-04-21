import turtle
schermo=turtle.Screen()
def stampa(indice):
    lati=int(input("inserisci il numero dei lati : "))    
    gradi=(180*(lati-2))/lati
    var=gradi-90
    for _ in range(lati):
        listaTurtle[indice].forward(100)
        listaTurtle[indice].right(90-var)


listaTurtle,k=[turtle.Turtle(),turtle.Turtle()],0
listaTurtle[1].right(180)

for _ in range(2):
    stampa(k)
    k+=1

schermo.exitonclick()
