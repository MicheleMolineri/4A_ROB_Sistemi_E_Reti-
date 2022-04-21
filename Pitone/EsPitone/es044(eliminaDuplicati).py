lista,listaSingoli=[1,2,3,2,3,4,5],[]

for elemento in lista:
    if elemento not in listaSingoli:
        listaSingoli.append(elemento)

print(listaSingoli)
