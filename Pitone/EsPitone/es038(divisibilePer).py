# Scrivi un programma in Python in cui chiedi all’utente un numero
# e comunichi se esso è divisibile per 2, oppure per 3, oppure per 5,
# oppure per nessuno di essi.

num=int(input("inserisci un numero : "))

if(num%2==0):
    print("E' divisibile per 2 \n")
if(num%3==0):
    print("E' divisibile per 3 \n")
if(num%5==0):
    print("E' divisibile per 5 \n")