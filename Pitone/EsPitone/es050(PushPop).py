def push(pila,elemento):
    pila.append(elemento)

def pop(pila):
    if len(pila)!=0:
        return pila.pop()
    else:
        return None
    

risp="s"
pila=[]

while (risp =="s") : 
    num=int(input("inserisci un numero da aggiungere : "))
    push(pila,num)
    risp=input("vuoi inserirne altri ? [s] [n] : ")


elemento = pop(pila)
while elemento != None:
    print(elemento)
    elemento = pop(pila)

