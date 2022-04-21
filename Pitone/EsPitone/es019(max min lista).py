lista=[1,2,3,4,5,6,7,8]

max,min=lista[0],lista[0]

for elemento in lista :
    if(min>elemento):
        min=elemento
    elif(max<elemento):
        max=elemento
    
print (lista)  
print(f"L'elemento maggiore è {max} l'elemento minore è {min}")

        

    

