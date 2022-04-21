import sys, pygame
from numpy import unicode_
from time import time
pygame.init()

width, height = 640, 480
size=(width, height)
speed = [1, 1]
black = (0, 0, 0)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("./es061_PyGame/intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        speed=10
        if event.type == pygame.QUIT: sys.exit()
        if event.type==pygame.KEYDOWN:
            print( event.__dict__["unicode"])
            if(event.__dict__["unicode"]=="w"):
                ballrect = ballrect.move(0,-speed)
            elif(event.__dict__["unicode"]=="s"):
                ballrect = ballrect.move(0,speed)
            elif(event.__dict__["unicode"]=="d"):
                ballrect = ballrect.move(speed,0)
            elif(event.__dict__["unicode"]=="a"):
                ballrect = ballrect.move(-speed,0)
        if ballrect.left < 0 :
            ballrect = ballrect.move(speed,0)
        if ballrect.right > width:
            ballrect = ballrect.move(-speed,0)
        if ballrect.top < 0 :
            ballrect = ballrect.move(0,speed)
        if ballrect.bottom > height:
            ballrect = ballrect.move(0,-speed)


    #ballrect = ballrect.move(speed)
    
    
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
