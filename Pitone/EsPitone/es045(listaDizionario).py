"""Scrivere un programma che data una lista qualsiasi la trasformi in un
dizionario avente come chiavi gli indici della lista e come valori gli
elementi."""

lista,dizionario=["a","b","c"],{}

for indice,elemento in enumerate(lista):
    dizionario[indice]=elemento
    
#   dict comprienscion
#   dizionario={x:elemento for x,elemento in enumerate(lista)}

print(dizionario)
