def ePrimo(num):
    div,count=2,0

    while div<=num/2 and count==0:
        if num%div==0:
            count+=1
        else:
            div+=1
    if count==0:
       return True 
    else:
       return False

testo=open("./testo.txt","w")
num,nNumPrimi=2,0
while(nNumPrimi <=100):
    if((ePrimo(num))):
        testo.write(str(num) +"\n")
        nNumPrimi+=1
    num+=1