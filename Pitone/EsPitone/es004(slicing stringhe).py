#SLICING Stringhe
""""

print(f"Il primo carattere è {stringa[0]}")
print(f"L'ultimo carattere è {stringa[-1]}")
print(stringa[3:9])#prende i caratteri del 3 all'8   9 escluso
print(stringa[0:7])
print(stringa[6: ])#stampa dal 6 carattere fino alla fine
print(stringa[ :-2])#stampo dall'inizio fino alla fine meno 2
print(stringa[2:14:2])#stampa da due a 13 a balzi di due
print(stringa[ : :-1])#stampa invertito

"""
stringa="Classe quarta A robotica" 

#  stringa[10]="B"  le stinghe in python sono IMMUTABILI
#TypeError 'str' object does not support item assignment

stringaNuova = stringa[0:14] + "B"+ stringa[15:]
print(f"La stringa originale è : {stringa}")
print(f"La stringa modificata è : {stringaNuova}")



