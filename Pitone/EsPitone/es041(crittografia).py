def cerca(lettera):
    continua = True
    k = 0
    while continua == True:
        if lettera != lista[k]:
            k+=1
            continua = True
        else:
            continua = False
    return (k)

stringa = input("inserisci la stringa da crittografare: ")
stringaMaiuscola = stringa.upper()
lista = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
num = int(input("inserisci il numero di scorrimenti : "))
lungh=27
stringaCrittografata = ""
for lettera in stringaMaiuscola:
    indice = cerca(lettera)
    
    stringaCrittografata = stringaCrittografata + lista[(indice+lungh)%num]
print(f"stringa crittografata : {stringaCrittografata}")

listaStringhe = []
stringaDec = ""
for k in range(1,lungh-1):
    for lettera in stringaCrittografata:
        indice = cerca(lettera)
        stringaDec = stringaDec + lista[(indice-k)%lungh]
    listaStringhe.append(stringaDec)
    stringaDec = ""
print(listaStringhe)



