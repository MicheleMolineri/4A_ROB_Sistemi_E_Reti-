griglia={0:" ",1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" " }
finePartita=False

def controlloVittoria(giocatore):
    win=False
    if(griglia[0]==griglia[1]==griglia[2] == giocatore):
        print(f"ha vinto il giocatore {giocatore}")
        win=True
    elif(griglia[3]==griglia[4]==griglia[5] == giocatore):
        print(f"ha vinto il giocatore {giocatore}")
        win=True
    elif(griglia[6]==griglia[7]==griglia[8] == giocatore):
        print(f"ha vinto il giocatore {giocatore}")
        win=True
    elif(griglia[0]==griglia[3]==griglia[6] == giocatore):
        print(f"ha vinto il giocatore {giocatore}")
        win=True
    elif(griglia[1]==griglia[4]==griglia[7] == giocatore):
        print(f"ha vinto il giocatore {giocatore}")
        win=True
    elif(griglia[2]==griglia[5]==griglia[8] == giocatore):
        print(f"ha vinto il giocatore {giocatore}")
        win=True
    elif(griglia[0]==griglia[4]==griglia[8] == giocatore):
        print(f"ha vinto il giocatore {giocatore}")
        win=True
    elif(griglia[6]==griglia[4]==griglia[2] == giocatore):
        print(f"ha vinto il giocatore {giocatore}")
        win=True
    return win 

def stampaGriglia():
    print(f"{griglia[0]}   |   {griglia[1]}   |   {griglia[2]} \n ---------------- \n  ")
    print(f"{griglia[3]}   |   {griglia[4]}   |   {griglia[5]} \n ---------------- \n  ")
    print(f"{griglia[6]}   |   {griglia[7]}   |   {griglia[8]} \n  ")

def controlloPosizione(posizione,giocatore):
    libero=True
    while(libero ):
        if(posizione<=8 and posizione>=0 and griglia[posizione] == " "):
            griglia[posizione]=giocatore
            libero=False
        else:
            print("Non puoi mettere in questa posizione \n") #controllare che la cella sia libera
            posizione=int(input("Reinserisci la posizione : ") )
            
stampaGriglia() 
giocatore1,giocatore2="X","O"
vittoria=False

while (vittoria==False):
    posizione1=int(input(" Giocatore 1 inserisci la posizione : ") )    #chiedere mossa giocatore 1
    controlloPosizione(posizione1,giocatore1)
    stampaGriglia()          #stampagriglia
    vittoria=controlloVittoria(giocatore1)       #controllo vittoria
    if(vittoria==False):
        posizione2=int(input(" Giocatore 2 inserisci la posizione : ") )    #chiedere mossa giocatore 2
        controlloPosizione(posizione2,giocatore2)   #controllare che la cella sia libera
        stampaGriglia()
        vittoria=controlloVittoria(giocatore1)   #controllo vittoria
