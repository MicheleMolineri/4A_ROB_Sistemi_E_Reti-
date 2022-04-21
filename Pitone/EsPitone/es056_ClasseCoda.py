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

c1=Coda()
c1.enqueue("ciao")
c1.enqueue("1")
c1.enqueue("2")
c1.dequeue()
c1.stampa()