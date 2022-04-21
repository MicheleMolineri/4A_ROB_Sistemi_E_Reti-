def sommaMolt(x,y):
    somma=x+y
    molt=x*y
    return {"somma":somma,"moltiplicazione":molt} 

a,b=10,4
dizionario=sommaMolt(a,b)
print(dizionario)