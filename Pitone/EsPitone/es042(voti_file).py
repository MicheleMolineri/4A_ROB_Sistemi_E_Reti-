"""segreteria di una scuola, inserisci cognome di alunno e voto di condotta per tutti gli alunni.
Vengono salvati su file cognome, voto però per privacy il cognome solo prima lettera seguita da  * """
def main ():
    file,max_alunni=open("./file.txt","w"),int(input("inserisci il numero di alunni nella classe : "))
    for alunno in range(max_alunni):
        nome,cognome,voto=input(" inserisci il nome : "),input(" inserisci il cognome : "),float(input("inserisci il voto di condotta : "))
        num=len(cognome)-1
        file.write(nome + " , " + cognome[0]+ ((num)*"*") + " , " +str(voto) +"\n")

if __name__=="__main__":
    main()
