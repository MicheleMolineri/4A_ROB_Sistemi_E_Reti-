# Utilizzando le list comprehension scrivi un programma 
# che crei una lista con tutte le potenze di due minori o 
# uguali a un valore inserito dall’utente. Stampa la lista.

num=int(input("Inserisci un numero : "))
listaPotenze=[2**k for k in range(num) if(2**k<=num)]
print(listaPotenze)