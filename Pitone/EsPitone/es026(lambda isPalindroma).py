controllo=lambda str:(str == str[::-1])
s=input("inserisci una  stringa : ")
ok=controllo(s)

if(ok):
    print("E' palindroma")
else:
    print("Non è palindroma ")