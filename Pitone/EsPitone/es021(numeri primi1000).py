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

conta,lista=0,[]

for num in range(2,1000):
    if((ePrimo(num))):
        lista.append(num)
        conta+=1

print(lista)
print(f"Inumeri primi minori di 1000 sono : {conta}")

