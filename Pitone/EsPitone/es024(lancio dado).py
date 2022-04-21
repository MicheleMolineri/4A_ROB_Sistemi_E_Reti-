import random
lancio1,lancio2=1,0

while(lancio1 != lancio2):
    lancio1 = random.randint(1,6)
    lancio2 = random.randint(1,6)

    if(lancio1>lancio2):
        print(f"Ha vinto giocatore 1 con un lancio da {lancio1} ")
    else:
        print(f"Ha vinto giocatore 2 con un lancio da {lancio2} ")
