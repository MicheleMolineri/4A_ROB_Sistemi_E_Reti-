voto=int(input("inserisci il tuo voto : " ))
if voto >= 8:
    print(" molto bene ")
elif voto >=7 & voto<8 :
    print("bene")               # NELLA IF POSSO METTERE QUANTE ELIF VOGLIO 
elif voto >=6 & voto<7 :
    print("abbastanza bene")
else : 
    print("insuffieciente")        # DOPO LA ELSE NON POSSO METTERE ULTERIORI CONDIZIONI