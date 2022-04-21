"""
Il file prezzi.csv (separatore ;) contiene le serie storiche mensili dei
prezzi di alcuni generi alimentari dal Settembre 2011 a Dicembre
2016.Immagina una spesa costituita da 5 generi alimentari a tua
scelta e crea una lista contenente la serie storica del prezzo della tua
spesa ottenuta sommando i prezzi dei generi alimentari scelti.
Calcola mese / anno in cui la tua spesa ha costi minimi e massimi.
"""

def inserisciData():    
    anno = input("In che anno hai fatto la spesa: ")   
    mese = input("In che mese hai fatto la spesa: ")
    return mese[0].upper()+mese[1:],anno

def inserisciArticoli(): 
    lista = []
    for _ in range (5):
        articolo =  str(input("inseririsci un articolo: "))
        lista.append(articolo)
    return lista

def caricaMatrice(righe):
    matrice = []
    for linea in righe: 
        stringa = linea.split(';')
        matrice.append(stringa)
    return matrice

f = open("./prezzi.csv","r")
righe = f.readlines()

matrice = caricaMatrice(righe)
riga,colonna = 0,0

mese,anno =inserisciData()
listaArticoli =inserisciArticoli()        
prezzoSpesa,prezzoMax,prezzoMin = 0,0,0
annoMax,meseMax,annoMin,meseMin = "","","",""

indiceProdotto = [] #memorizza la colonna dei prodotti

for elemento in listaArticoli:  
    for r in range(len(matrice)):
        for c in range(len(matrice[r])):
            if matrice[r][c] == elemento:  # si trova la colonna dell'ariticolo
                colonna = c                
                if matrice[r][0] == anno and matrice[r][1] == mese: #ricerca per mese anno
                    riga = r
                    prezzoSpesa += float(matrice[riga][colonna]) 
    
    indiceProdotto.append(colonna) 

for r in range(1,len(matrice)):  
    prezzo = 0                   
    for indice in indiceProdotto:   
        prezzo += float(matrice[r][indice])
    if prezzo > prezzoMax:
        prezzoMax = prezzo
        annoMax = matrice[r][0]
        meseMax = matrice[r][1]
    if prezzo < prezzoMin:
        annoMin = matrice[r][0]
        meseMin = matrice[r][1]
        prezzoMin = prezzo

print(f"costo spesa oggi { round(prezzoSpesa,2)}")
print(f"costo spesa maggiore: {meseMax}  {annoMax}  {round(prezzoMax,2)}€")
print(f"costo spesa minore: {meseMin}  {annoMin}  {round(prezzoMin,2)}€")
f.close()