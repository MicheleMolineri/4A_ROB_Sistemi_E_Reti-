isPalindroma=lambda str:(str == str[::-1])

lista,listaMaiuscole,listaPalindrome=["parola1","anna","reer","Parola2","Parola3"],[],[]

#metodo list comprehescion 
listaMaiuscole = [ parola for parola in lista if parola[0].isupper()]
listaPalindrome= [parola for parola in lista if isPalindroma(parola)]

"""

metodo classico

for parola in lista:
    if(isPalindroma(parola)):
        listaPalindrome.append(parola)
    
    if(parola[0].isupper()):
        listaMaiusole.append(parola)

"""        

print(f"Lista iniziale {lista} , Lista maiuscole  {listaMaiuscole} , lista palindromi  {listaPalindrome}")



