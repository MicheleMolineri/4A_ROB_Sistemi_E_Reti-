import matplotlib.pyplot as plt

f = open("./PitoneGrafici/file.csv","r")
lines = f.readlines()
X,y1,y2 = [],[],[]

for line in lines[1:]:
    values = line.split(",")
    
    X.append(values[0])
    y1.append(float(values[-2]))
    y2.append(float(values[-1]))



fig,axs = plt.subplots(nrows=2,ncols=1,figsize=(10,10)) #ritorna una fiugura e un asse

#crea il grafico con linea rossa  ro -> fa pallini rossi r-linee unite ro- pallini uniti a linee
#r -- tratteggiato
axs[0].plot(X,y1,'bd-',linewidth = 2 )
axs[0].grid()
axs[0].set_title("grafici voti e ore sudio")
axs[0].set_xlabel("Mesi")
axs[0].set_ylabel("Ore Studio",color='blue')


axs[1].plot(X,y2,'ro-',linewidth = 2 )
axs[1].grid()
axs[1].set_xlabel("Mesi")
axs[1].set_ylabel("Voti",color='red')

#plt.savefig("grafico.pdf")     salva il file in formato
plt.show()