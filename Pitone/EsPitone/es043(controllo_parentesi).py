
def controlloErrori(stringa):
    listaParentesi=[]
    aperte,chiuse,ok = ["(","[","{"],[")","]","}"],True #assegno True ad ok e se dopo i controlli non varia la str è corretta
    dizionario = {"(":")", "[":"]", "{":"}", ")":"(", "]":"[", "}":"{"}
    
    for lettera in stringa: #scorro tutte le lettere della stringa
        if lettera in aperte: #controllo se la lettera appartiene alla lista delle aperte
            listaParentesi.append(lettera)    
        elif lettera in chiuse: # controllo se appartiene alle chiuse
            if len(listaParentesi) != 0:
                if lettera != dizionario[listaParentesi.pop()] : #se la parentesi chiusa è diversa dalla parentesi precedente torna false
                    ok = False
            else:
                ok = False

    if len(listaParentesi) > 0:  # se la lunghezza è maggiore di 0 ci sono ancora parentesi aperte o chiuse
        ok = False


    return ok #se dopo tutti i controlli ok non cambia la str è corretta  

def main():
    str = input("Inserisci la stringa: ")
    ok = controlloErrori(str)
    if ok :
        print("Stringa corretta")
    else:
        print("Stringa Errata")


if __name__ == "__main__":
    main()
        
