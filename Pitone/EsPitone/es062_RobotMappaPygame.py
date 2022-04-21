
import random,os,pygame
import fontTools

pygame.init()
RED,GREEN,BLACK,MARGIN,DIM,SIZECELLA = (255, 0, 0),(0,255,0),(0,0,0),1,     10      ,    40
widthCampo, heightCampo, spostamento= DIM*SIZECELLA+8*MARGIN,DIM*SIZECELLA+8*MARGIN,SIZECELLA+MARGIN
size = (widthCampo, heightCampo)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Campo di gioco")


def creaMappa(dim):
    matrice = [[0]*dim for _ in range(dim)]
    for r in range(dim):
        for c in range(dim):
            matrice [r][c]=random.choice([0,1])
    return matrice

def disegnaMappa(mappa):

    for riga in range(len(mappa)):
        for colonna in range(len(mappa)):
            color = RED
            if mappa[riga][colonna] == 0:
                color = GREEN  
            pygame.draw.rect(screen,color, [(SIZECELLA + MARGIN) * colonna+MARGIN,(SIZECELLA+MARGIN) * riga+MARGIN,SIZECELLA,SIZECELLA])
    
def posizionaRobot(mappa,robot,rect):
    posiz = False
    for riga in range(len(mappa)):
        for colonna in range(len(mappa)):
            if mappa[riga][colonna] == 0 and posiz == False:
                x,y = colonna*SIZECELLA + MARGIN*colonna,riga*SIZECELLA + MARGIN*riga
                screen.blit(robot,(x,y))
                rect = rect.move(x,y)
                posiz = True
    return x,y

def possoPosizionareRobot(mappa,x,y):
    puoi ,r,col= False , y/(SIZECELLA+MARGIN), x/(SIZECELLA+MARGIN)
    if r<DIM and col<DIM and r>=0 and col>=0 and mappa[int(r)][int(col)] == 0:
        puoi = True
    return puoi

def gioca(mappa):
    pygame.init()

    robot = pygame.image.load('./robot.png')
    robot = pygame.transform.scale(robot,(30,30))
    robotRect,posizionato = robot.get_rect(),False
    disegnaMappa(mappa)
    x,y = posizionaRobot(mappa,robot,robotRect)

    while True:
        
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type==pygame.KEYDOWN:
                #print( event.__dict__["unicode"])
                
                if(event.__dict__["unicode"]=="w"):
                    if y-spostamento >= 0 and possoPosizionareRobot(mappa,x,y-spostamento):    
                        y-=spostamento
                        disegnaMappa(mappa) 
                        screen.blit(robot,(x,y))
                        robotRect = robotRect.move(0,-spostamento)

                elif(event.__dict__["unicode"]=="s"):
                    if y+spostamento <= heightCampo  and possoPosizionareRobot(mappa,x,y+spostamento):
                        y+=spostamento
                        robotRect = robotRect.move(0,+spostamento)
                        disegnaMappa(mappa) 
                        screen.blit(robot,(x,y))
                elif(event.__dict__["unicode"]=="d"):
                    if x+spostamento <= widthCampo and possoPosizionareRobot(mappa,x+spostamento,y):
                        x+=spostamento
                        robotRect = robotRect.move(0,+spostamento)
                        disegnaMappa(mappa) 
                        screen.blit(robot,(x,y))
                elif(event.__dict__["unicode"]=="a"):
                    if x-spostamento >= 0 and possoPosizionareRobot(mappa,x-spostamento,y):
                        x-=spostamento
                        robotRect = robotRect.move(0,-spostamento)
                        disegnaMappa(mappa) 
                        screen.blit(robot,(x,y))
          
        pygame.display.flip()

def main():
    #os.system('clear')
    mappa  = creaMappa(DIM) 
    gioca(mappa)

if __name__ == "__main__":
    main()

