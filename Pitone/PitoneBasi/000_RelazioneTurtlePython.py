"""
Una libreria è un insieme di funzioni e metodi che semplificano la programmazione
La libreria Python turtle contiene tutti i metodi e le funzioni per creare delle immagini.
Per accedere a una libreria Python, bisogna importarla nell' ambiente Python, in questo modo:
"""

import turtle

"""
Turtle è una libreria Python preinstallata che consente di creare immagini e forme fornendo loro una tela virtuale.
La freccia sullo schermo che si usa per disegnare si chiama turtle e questo è ciò che dà il nome alla libreria.
la turtle è un modo semplice ma versatile per comprendere i concetti di Python.


Turtle è una libreria grafica, quindi bisogna creare una finestra separata per eseguire ogni comando di disegno.
Si creare questa schermata inizializzando una variabile Turtle.

"""

schermo = turtle.Screen()    #inizializzazione variabile   apparirà uno schermo con una freccia  al centro
tarataruga = turtle.Turtle()    #inizializzazione variabile turtle

"""
dopo aver creato lo schermo e la tartaruga (freccia) possiamo farla muovere con le seguenti funzioni
"""

tarataruga.right(90) # la tartaruga gira a destra di 90°
tarataruga.forward(100)  # la tartaruga va avanti di 100 unità
tarataruga.left(90) # la tartaruga gira a sinistra di 90°
tarataruga.backward(100) # la tartaruga va indietro di 100 unità
schermo.reset #pulisce lo schermo

"""
Lo schermo è diviso in quattro quadranti. Il punto in cui la tartaruga è inizialmente posizionata all'inizio del tuo programma è (0,0).
Per spostare la tartaruga in qualsiasi altra area dello schermo bisogna usare .goto() e inserire le coordinate
Chiamando la funzione .home() lei tornerà alle coordinate (0,0) 
"""

x,y=10,20
tarataruga.go(x,y) # adesso la tartaruga si posizionerà in queste coordinate
tarataruga.home # la posizione viene resettata

"""
La turtle viene usata per la creazione di forme reali.
Si può iniziare disegnando poligoni poiché sono tutti costituiti da linee rette collegate a determinati angoli
"""

tarataruga.fd(100)      # forma abbreviata per  .forward()
tarataruga.rt(90)       # forma abbreviata per  .right()
tarataruga.fd(100)
tarataruga.rt(90)
tarataruga.fd(100)
tarataruga.rt(90)
tarataruga.fd(100)


"""
Si posono anche creare  cerchi con .circle
"""
raggio=50
tarataruga.circle(raggio) 
