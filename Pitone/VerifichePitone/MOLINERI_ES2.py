"""Create una classe IPAddress che permetta di rappresentare indirizzi ip in notazione decimale puntata.
 La classe deve essere dotata di un metodo che permetta di ottenere la rappresentazione binaria dell'indirizzo 
 ip e di un metodo che permetta di determinare se l'indirizzo ip è una subnet mask 
 (in caso affermativo il metodo ritorna True, altrimenti False). 
 Ricordate che una subnet mask è un indirizzo ip costituito da soli 1 nella prima parte e da soli 0
  nella seconda parte....
La classe deve essere dotata di un terzo metodo che verifica la validità di un indirizzo ip:
 per esempio 300.123.10.19 non è un ip valido.
Il programma deve avere nome file ES2_COGNOME.py."""

from operator import truediv


class IPAddress ():

    ipDec=""
    ipBin=""
    
    def __init__(self) -> None:
        self.ipDec=input("inserisci un ip : ")

    def dec2bin(numDec,nbit):
        s=bin(numDec)[2:]
        s="0"*(nbit-len(s))+s
        return s

    
    def bin2dec(self,numBin):
        numDec = 0
        for k,elem in enumerate(numBin[::-1]):
            numDec+= int(elem)*(2**k)
        return numDec

    def IP_bin2dec(self,ipBin):
        ipDec,n,nd="",0,8
        for _ in range (4):
            ipDec+=str(self.bin2dec(ipBin[n:nd]))+"."
            n+=8
            nd+=8
        self.ipDec=ipDec[:-1]
        return ipDec[:-1]
    
    
        
        


ip=IPAddress()
ip.controlloSub()