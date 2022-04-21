
lista = [3,3.23,"ciao"]
print(lista)

numeriPrimi=[2,3,5,7,11,13]
print(numeriPrimi[1:-1])
lista[1] = 2.645
print(lista)

#aggiungo una stinga alla lista
lista.append("mariuccia")
print(lista)
numeriPrimi.append(17)
print(numeriPrimi)

print(f"La lunghezza è {len(numeriPrimi)}")

# concatenare liste
altri_numeri_primi=[19,23,29]
molti_numeri_primi= numeriPrimi+altri_numeri_primi
print(molti_numeri_primi)

#ripete la llista 5 volte
print(5*altri_numeri_primi)


