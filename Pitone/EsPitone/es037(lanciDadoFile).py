import random
f=open("./file.txt","w")

listaAlice=[random.randint(1,6) for lancio in range(10) ]
listaBob=[random.randint(1,6) for lancio in range(10) ]

f.write("Alice | Bob\n")

for lancio in range(10):
    f.write("  "+str(listaAlice[lancio])+"   ,  "+ str(listaBob[lancio])+"\n")
    