lista=[ (a*b) for a in range(11) for b in range (11) ]
a,b=0,11

for k in range(11):
    print(lista[a:b])
    a+=11
    b+=11

