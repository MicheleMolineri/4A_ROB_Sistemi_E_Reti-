liste=["ciao","boh","parola","parolona"]
lungh=0
for parola in liste :
    if(len(parola)>lungh):
        lungh=len(parola)
        strMax=parola

print(strMax)