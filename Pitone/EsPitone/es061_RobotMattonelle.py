
import random,os

campDaGIoco =[[0,0,1,0], 
            [1,0,1,1],
            [1,0,0,0],
            [1,1,1,1]]
            
def contaCelleLibere(campo):
    #numerare celle libere
    dizionarioAdiacenze, conta={}, 0

    for r in range(len(campo)):
        for c in range(len(campo)):
            if campo[r][c] == 0:
                conta += 1
                dizionarioAdiacenze[conta-1] = []

    return conta,dizionarioAdiacenze

def creaMappa(dim):
    matrice = [[0]*dim for _ in range(dim)]
    for r in range(dim):
        for c in range(dim):
            matrice [r][c]=random.choice([0,1])
    return matrice

def generaProssimita(campo,dizionarioProssimita):
    movimentiFissi , cella = [(0,1),(0,-1),(1,0),(-1,0)] , 0
    
    for k in range(len(campo)):
        for j in range(len(campo)):
            if(campo[k][j] == 0):
                for mossa in movimentiFissi:
                    if k + mossa[0]<len(campo) and j+mossa[1]<len(campo):
                        if (campo[k+mossa[0]][j+mossa[1]]) == 0:
                            if k+mossa[0]>=0 and j+mossa[1]>=0:
                                dizionarioProssimita[cella] += [[k+mossa[0],j+mossa[1]]]
                    
                cella+=1
        
    return dizionarioProssimita  


def main():
    #os.system('clear')
    campDaGIoco=creaMappa(4)
    nCelleLibere,dizionarioAdiacenze = contaCelleLibere(campDaGIoco)
    dizionarioAdiacenze = generaProssimita(campDaGIoco,dizionarioAdiacenze)

    for chiave in dizionarioAdiacenze:
       print(f"{chiave} comunica con {dizionarioAdiacenze[chiave]}")


if __name__ == "__main__":
    main()



