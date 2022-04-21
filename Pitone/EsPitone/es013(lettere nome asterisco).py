nome=input("inserisci il tuo nome : ")

print("*"+nome[1:]) # stampo * poi il resto del nome

num = len(nome)
print(nome[0]+ ((num-1)*"*"))  # stampo iniziale più asterischi lungh nome-1
