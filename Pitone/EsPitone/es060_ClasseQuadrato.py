import turtle

class Quadrato():

    def __init__(self,x1,y1,lato) -> None:
        self.x = x1
        self.y = y1
        self.l = lato

    def getLato(self):
        return self.l

    def getArea(self):
        return self.l*self.l

    def getPerimetro(self):
        return self.l * 4

    def verificaPunto(self,xp,yp):
        if (xp>self.x+self.l or xp < self.x and yp>self.y + self.l | yp<self.y):
            print("Il punto è esterno al quadrato \n")
        else :
            print("Il punto è interno al quadrato \n")

    def disegnaQuadrato(self):
        screen=turtle.Screen()
        quadrato=turtle.Turtle()
        screen.bgcolor("black")
        quadrato.color("white")

        for _ in range(4):
            quadrato.fd(self.l*10) #lunghezza lato scalato per renderlo più visibile
            quadrato.left(90)
        turtle.exitonclick()



q1=Quadrato(0,0,15)

q1.disegnaQuadrato()
print(f"Lato : {q1.getLato()} , Perimetro : {q1.getPerimetro()} , Area : {q1.getArea()}")
xp,yp=int(input("inserisci la x di un punto : ")),int(input("inserisci la y di un punto : "))
q1.verificaPunto(xp,yp)


