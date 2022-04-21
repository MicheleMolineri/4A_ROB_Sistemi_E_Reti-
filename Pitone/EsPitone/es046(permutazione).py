"""
Scrivere un programma che data una lista ne stampi una sua
permutazione casuale.
"""

import random


lista,listaRandomizzata=[1,2,3,4,5,6,7,8,8],[]

for _ in range(len(lista)):
    elemento = random.randint(0,len(lista)-1)
    listaRandomizzata.append(lista[elemento])
    lista.remove(lista[elemento])

print (listaRandomizzata)

