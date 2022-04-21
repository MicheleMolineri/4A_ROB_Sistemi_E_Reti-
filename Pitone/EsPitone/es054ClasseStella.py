import turtle,random

class Stella() :
    
    def __init__(self) -> None:
        turtle.Turtle()
        screen=turtle.Screen()
        turtle.speed(0)
        turtle.color("yellow")
        screen.bgcolor("black")
        
    
    def disegnaStella(self,x,y):
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
        GRAD,lung=144,random.randint(10,25)
   
        for _ in range(5):
           turtle.forward(lung)
           turtle.right(GRAD)


def main():
    for _ in range(50):
        s=Stella()
        s.disegnaStella(random.randint(-300,300),random.randint(-300,300))
    turtle.exitonclick()


if __name__=="__main__":
    main()