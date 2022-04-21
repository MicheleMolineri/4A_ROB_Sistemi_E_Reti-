parola=input("inserisci una parola : ")
#stampa lettera finale e iniziale
print(f"lettera iniziale : {parola[0]} lettera finale {parola[-1]}")
#stampa parola senza iniziali e finali
print(parola[1:-2])
#una lettera si e una no
print(parola[::2])
#parola invertita
print(parola[: :-1])
#carattere ? al posto della 3 lettera
str="parolalunga"
strnew=str[0:2]+"?"+str[3:]

print(f"La stringa originale è : {str}")
print(f"La stringa modificata è : {strnew}")
