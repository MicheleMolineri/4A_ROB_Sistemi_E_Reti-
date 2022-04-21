coda=[0,1,2,3,4,5,6,7]

def enqiu (coda,elemento):
    coda.append(elemento)

def deqiu(coda):
    if len(coda)!=0:
        return coda.pop(0)
    else:
        return None


cliente1={ "nome" : "GIANNI", "id":123}
cliente2={ "nome" : "GIANNA", "id":456}

codaClienti=[]
enqiu(codaClienti,cliente1)
enqiu(codaClienti,cliente2)

print(codaClienti)