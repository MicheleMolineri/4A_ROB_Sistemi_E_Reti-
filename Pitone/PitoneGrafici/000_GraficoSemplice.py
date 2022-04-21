import matplotlib.pyplot as plt

X=[x for x in range(10)]
y=[x**2 for x in X]
y2=[x**4 for x in X]

fig,ax = plt.subplots(figsize=(10,10)) #ritorna una fiugura e un asse

#crea il grafico con linea rossa  ro -> fa pallini rossi r-linee unite ro- pallini uniti a linee
#r -- tratteggiato
ax.plot(X,y,'rd--')
ax.plot(X,y2,'bd--')
ax.grid()

ax.set_title("Primo grafico")
ax.set_xlabel("Etichetta asse x")
ax.set_ylabel("Etichetta asse y")

plt.show()