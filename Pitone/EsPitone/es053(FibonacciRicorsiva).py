"""
Scrivere una funzione Python ricorsiva che permetta di stampare i numeri di Fibonacci minori di un valore scelto dall'utente
"""

def fibonacci(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibonacci(n-1) + fibonacci(n-2))  

max = int(input("Inserisci un numero : "))  

i=1
for _ in range(max):
    print(fibonacci(i)) 
    i+=1
   