str=input("inserisci una  stringa : ")
controllo = lambda str : (str[0].isupper())
ok=controllo(str)
if(ok):
    print("Inizia con una maiuscola ")
else:
    print("Non inizia con una maiuscola ")