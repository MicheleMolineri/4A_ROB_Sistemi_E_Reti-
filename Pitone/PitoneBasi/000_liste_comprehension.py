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


listaPrimi=[k for k in range(2,1003) if ePrimo(k)]
print(listaPrimi)