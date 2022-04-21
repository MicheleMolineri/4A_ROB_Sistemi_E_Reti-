import es057_Pile_Code as pc  # alias  

coda=pc.Coda()
codaInvertita=pc.Coda()
pila=pc.Pila()
answer="s"

while(answer =="s"  ):
    elem=input("Inserisci un elemento nella coda : ")
    coda.enqueue(elem)
    pila.push(elem)
    coda.stampa()
    answer=input("Vuoi inserire altri elementi [s] [n] : ")

for _ in range(len(pila.pila)):
    codaInvertita.enqueue(pila.pop())

codaInvertita.stampa()
