class Coda():
    def __init__(self) -> None:
        self.coda=[]

    def enqueue(self,elemento):
        self.coda.append(elemento)

    def dequeue(self):
        if len(self.coda)>0:
            return self.coda.pop(0)
        else:
            print("La Coda non ha più elementi")
            return None

    def stampa(self):
        print(self.coda)


class Pila():
    def __init__(self):
        self.pila=[]

    def push(self,elemento):
        self.pila.append(elemento)

    def pop(self):
        if len(self.pila)>0:
            return self.pila.pop()
        else:
            print("La pila non ha più elementi")
            return None

    def stampa(self):
        print(self.pila)

def main():
    p=Pila()  
    p.push("ciao")
    p.push(2)
    p.stampa()

    c=Coda()
    c.enqueue(5)
    c.enqueue(6)
    c.stampa()


if __name__=="__main__":
    main()