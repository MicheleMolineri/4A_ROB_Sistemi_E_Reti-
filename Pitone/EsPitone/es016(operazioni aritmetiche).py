oper=int(input("inserisci il numero dell'operazione vuoi fare "))
num1,num2=int(input("inserisci il primo numero : ")),int(input("inserisci il secondo numero : "))
if oper == 0:
    print(num1+num2)
elif oper==1:
    print(num1-num2)
elif oper == 2:
    print(num1*num2)
elif oper == 3 & num2!=0:
    print(num1/num2)
else:
    print("non è stato scelto un numero valido")
