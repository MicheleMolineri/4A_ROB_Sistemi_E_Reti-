import numpy as np
import os
mat = np.array([[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]])


def stampaCampo():
    print(mat)
    print("   0   1   2   3   4   5   6  ")


def controllo(posizione,giocatore):
    indiceBasso=5
    messo,pieno=False,False
    while (messo==False):
        if(mat[indiceBasso][posizione]==" "):
            messo=True
        else: indiceBasso-=1

        if(indiceBasso<0):
            print("Colonna piena non puoi più inserire ! ")
            pieno=True
    return pieno,indiceBasso


def inserisciPedina(giocatore):
   
    errore=True

    while(errore):
        posizione=int(input("giocatore : "+ giocatore + " inserisci la colonna in cui vuoi mettere la pedina : "))
        if posizione>=0 and posizione<=6:
            errore=False
        else:
            print("Numero colonna non valido. Reinserisci : ")

    pieno,indice=controllo(posizione,giocatore)
    if pieno==False:
        mat[indice][posizione]=giocatore
    else:
        newPieno=True
        while(newPieno):
            newPosition=int(input("giocatore : "+ giocatore + " inserisci la colonna in cui vuoi mettere la pedina : "))
            newPieno,newIndice=controllo(newPosition,giocatore)
        mat[newIndice][newPosition]=giocatore
    

def controlloVittoria(giocatore):
    riga,colonna,win = 5,0,False

    while win == False and riga>0 : #controllo orizzontale  
        if mat[riga][colonna]==mat[riga][colonna+1]==mat[riga][colonna+2]==mat[riga][colonna+3] and mat[riga][colonna]==giocatore:
            win = True
        else:
            colonna += 1
        if colonna == 4:
            colonna = 0
            riga -= 1

    riga,colonna = 5,0
    while win == False and colonna < 7: #controllo verticale 
        if mat[riga][colonna]==mat[riga-1][colonna]==mat[riga-2][colonna]==mat[riga-3][colonna] and mat[riga][colonna]==giocatore:
            win = True
        else:
            riga -= 1
        if riga == 2:
            colonna += 1
            riga = 5

    riga,colonna = 5,0
    while win == False and colonna < 4: #controllo /
        if mat[riga][colonna]==mat[riga-1][colonna+1]==mat[riga-2][colonna+2]==mat[riga-3][colonna+3] and mat[riga][colonna]==giocatore:
            win = True
        else:
            riga -= 1
        if riga == 2:
            colonna += 1
            riga = 5

    riga,colonna = 5,6
    while win == False and colonna > 2: #controllo \
        if mat[riga][colonna]==mat[riga-1][colonna-1]==mat[riga-2][colonna-2]==mat[riga-3][colonna-3] and mat[riga][colonna]==giocatore:
            win = True
        else:
            riga -= 1
        if riga == 2:
            colonna -= 1
            riga = 5

    if(win):print(f"{giocatore} ha vinto")

    return win
    

x,o,win,mosse="X","O",False,0


while(win==False):

    stampaCampo()
    if(mosse<48):
        inserisciPedina(x)
        mosse+=1
    else:
        print("Mosse esaurite. Pareggio")
    os.system('cls') #clear schermo
    win=controlloVittoria(x)
    

    if(win==False):
        stampaCampo()
        if(mosse<48):
            inserisciPedina(o)
            mosse+=1
        else:
            print("Mosse esaurite. Pareggio")
        os.system('cls') #clear schermo
        win=controlloVittoria(o)
        



    
