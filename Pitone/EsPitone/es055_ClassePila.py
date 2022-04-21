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


        
p1=Pila() #istanza classe pila
p1.push("ciao")
p1.stampa()
