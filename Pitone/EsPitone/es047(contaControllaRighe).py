"""
Il programma deve leggere il file e:
1. Contare il numero di righe totali
2. Contare il numero di chiamate alla funzione “printf”
3. Contare il numero di linee di commento.
"""

def controllaCommento(testo):
    contaCommenti,contaPrintf=0,0
    for linea in testo:
        for parola in linea.split():
            if parola == "//":
                contaCommenti+=1
            if parola == "printf":
                contaPrintf+=1
    
    return contaCommenti,contaPrintf



f=open("./file.txt","r")

testo = f.readlines()
nrighe=len(testo)
f.close()

cC,cP=controllaCommento(testo)
print(f"Le righe del file sono : {nrighe} , printf è stata chiamata {cP} n commenti : {cC})")

