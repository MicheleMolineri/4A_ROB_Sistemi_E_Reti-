
def bin2dec(numBin):
    numDec = 0
    for k,elem in enumerate(numBin[::-1]):
        numDec+= int(elem)*(2**k)
    return numDec

def dec2bin(numDec,nbit):
    s=bin(numDec)[2:]
    s="0"*(nbit-len(s))+s
    return s

def IP_dec2bin(ipDec):
    ipBin="" 
    splittato=ipDec.split(".")
    for elem in splittato:
        ipBin += dec2bin(int(elem),8)
    return ipBin

def IP_bin2dec(ipBin):
    ipDec,n,nd="",0,8
    for _ in range (4):
        ipDec+=str(bin2dec(ipBin[n:nd]))+"."
        n+=8
        nd+=8
    return ipDec[:-1]

def esisteErrore(ipBin,sub):
    ipBin=ipBin[::-1]
    
    listSub=[elmento for k,elmento in enumerate(ipBin) if(k<=sub)]

    if 1 in listSub: return True
    else:return False
    
def controlloIP(ip): 
    splittato=ip.split(".")
    for elem in splittato:
        if(int(elem)<=255):
            return False 
        else :
            return True 

def calcoloIpBroadcast(ipBin,sub):
    newIpBin = ipBin[:32-sub] 
    for _ in range(32-sub+1):
        newIpBin += "1"
    

    return IP_bin2dec(str(newIpBin))
    
def calcoloMax(ipBroad):
       return IP_bin2dec(str(ipBroad[:-1]+"0"))

def calcoloMin(ipBin):  
    return IP_bin2dec(str(ipBin[:-1]+"1"))

def calcolaSubnet(nNum):
    sub=""
    for _ in range(32-nNum):
        sub+="1"
    for _ in range(nNum):
        sub+="0"

    return IP_bin2dec(sub)


def main():

   #Chiedie utente ip rete 
   ipRete=input("Inserisci l'ip di rete : ")

   #controllo numeri ip
   while(controlloIP(ipRete)):
       ipRete=input("Numeri Indirizzo ip > 255  \nReinserisci l'ip di rete : ")

   #Chiede utente subnet mask 
   subnetMask=int(input("inserisci la subnet mask : /"))
   while(esisteErrore(ipRete,subnetMask)):
          subnetMask=int(input("Errore : subnet mask\ninserisci la subnet mask : /"))
   nNumeriSubnet = 32-subnetMask

   
   #Controllo IP rete convertire in binario guardare bit host(da n a 32)
   ipReteBin=IP_dec2bin(ipRete)
   print(f"Numeri a 0 subnet : {nNumeriSubnet}")

   while(controlloIP(ipReteBin)==False):
          ipRete=input("Indirizzo ip sbagliato \nReinserisci l'ip di rete : ")

   #Calcolo IP Broadcast
   broad=calcoloIpBroadcast(str(ipReteBin),nNumeriSubnet)
   print(f"Ip broadcast : {broad}")
   
   #Calcolo IP Max Min
   print(f"Ip Min : {calcoloMin(str(ipReteBin))}\nIp Max : {calcoloMax(IP_dec2bin(broad))}")
   print(f"Subnet : {calcolaSubnet(nNumeriSubnet)}")


if __name__ == "__main__":
    main()