def ePrimo(num):
    div,count=2,0

    while num/2 >= div and count==0:
        if num%div==0:
            count+=1
        else:
            div+=1
    if count==0:
       return True 
    else:
       return False

num=int(input("inserisci un numero : "))

if((ePrimo(num))):
    print("E' primo ")
else :
    print("Non è primo")
