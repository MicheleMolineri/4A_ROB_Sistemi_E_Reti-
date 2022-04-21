f=open("./covid.txt","r")
testo,dizionario=f.readlines(),{"A" : 0 ,"T": 0 ,"C": 0 ,"G": 0 }

for linea in testo:
        for lettera in linea:
           if lettera in dizionario:
               dizionario[lettera]+=1

print (dizionario)
