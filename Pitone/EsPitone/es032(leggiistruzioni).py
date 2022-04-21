import turtle

schermo = turtle.getscreen()
tarutaruga = turtle.Turtle()

f = open("./istruzioni.txt","r")
righe = f.readlines()

for riga in righe:

    ls = riga.split(":")
    valore =int(ls[1][:-1])
    
    if(ls[0]=="forward"):
        tarutaruga.forward(valore)
    elif(ls[0]=="left"):
        tarutaruga.left(valore)
    elif(ls[0]=="backward"):
        tarutaruga.backward(valore)
    elif(ls[0]=="right"):
        tarutaruga.right(valore)
    else:
        print("Comando non trovato")
    
    
f.close()
turtle.exitonclick()
    
    
    





