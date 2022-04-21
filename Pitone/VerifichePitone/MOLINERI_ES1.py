""" 
Il file medals.csv contiene tutte le medaglie assegnate alle recenti Olimpiadi Invernali. 
Ogni riga corrisponde a una medaglia assegnata. 
Scrivere un programma in Python3 che legga il file e calcoli quante medaglie d'oro, 
d'argento e di bronzo ha vinto l'Italia (colonna country=Italy). 
I tre valori devono essere salvati in un dizionario e il dizionario deve essere stampato.
Il programma deve avere nome file ES1_COGNOME.py."""

def caricaMatrice(righe):
    matrice = []
    for linea in righe: 
        stringa = linea.split(',')
        matrice.append(stringa)
    return matrice

f = open("./medals.csv","r")
righe = f.readlines()
dizionarioMedaglie={"oro" : 0,"argento":0,"bronzo": 0}
indiceColIta= [] #memorizza la colonna degli italiani

matrice,listaMedaglie,listaColonne= caricaMatrice(righe),["Gold","Silver","Bronze"],[]


for r in range(len(matrice)):
    
    for c in range(len(matrice[r])):
        #print(matrice[r][c])
        if matrice[r][c] == "Italy":  # si trova la  country  
            
            if matrice[r][0] == "Gold":  
                dizionarioMedaglie["oro"]+=1
            elif matrice[r][0] == "Silver":  
                dizionarioMedaglie["argento"]+=1
            elif matrice[r][0] == "Bronze":  
                dizionarioMedaglie["bronzo"]+=1


print(f"Medaglie Italiane : \nOro : { dizionarioMedaglie['oro'] }\nArgento : {dizionarioMedaglie['argento']}\nBronzo : {dizionarioMedaglie['bronzo']}")
