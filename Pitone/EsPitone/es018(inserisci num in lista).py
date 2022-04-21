risp="s"
lista=[0,1,2]
print(f"lista iniziale {lista}")
while (risp =="s") : 
    num=int(input("inserisci un numero da aggiungere : "))
    lista.append(num)
    print(lista)
    risp=input("vuoi inserirne altri ? [s] [n] : ")
print(f"lista finale {lista}")