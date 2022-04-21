indirizzi={"rob":"Smart-Robot","chi":"Chimica","mec":"Meccanica","tel":"telecomunicazioni"}

classi=["4arob","3achi","2atel","1arob","4bmec"]
indice=0
"""
for classe in classi:
    indice=indice+1
    indirizzo=indirizzi[classe[-3:]]                # metodo con contatore
    print(f"posizione {indice} lista : ")
    print(f"la classe {classe}  è dell'indirizzo {indirizzo}", end="\n\n")

"""
for indice, classe in enumerate(classi):
    indirizzo=indirizzi[classe[-3:]]                # metodo alternativo senza contatore
    print(f"posizione {indice+1} lista : ")
    print(f"la classe {classe}  è dell'indirizzo {indirizzo}", end="\n\n")





