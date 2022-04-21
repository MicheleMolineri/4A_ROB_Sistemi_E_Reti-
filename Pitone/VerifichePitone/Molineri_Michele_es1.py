import random

def spostamentoRandom():
    spostamento=0
    while(spostamento==0):
        spostamento = random.randint(-1,1)#casuale da -1 a 1 caso 0
    
    return spostamento

def spostamentoRandomFast():
    return random.choice([-1,1])

n=0
listaMovimenti=[spostamentoRandom() for _ in range(10)]# chiamo la funz spostamento random per il numero di secondi in 5 giorni
print(listaMovimenti)
sommaMovimenti=0
for movimento in listaMovimenti:
    sommaMovimenti+=movimento#sommo ogni elemento

print(f"La somma dei movimenti totali è : {sommaMovimenti}")