nome,cognome,data=input("Inserisci il nome : "),input("Inserisci il cognome : "),input("Inserisci il la data (day/month/year) : ")

dizionario={"nome" : nome ,"cognome" : cognome ,"data" : data }
testo=open("./testo.txt","w")

for chiave in dizionario: #dato che ho un dizionario scrivo chiave al posto di elemento
    testo.write(f"{dizionario[chiave]} \n")


