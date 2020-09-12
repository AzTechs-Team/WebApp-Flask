import pygame,sys
from pygame.locals import *

#initialize the pygae
pygame.init()
 
#Create a screen
screen=pygame.display.set_mode((1500,800))

#setting fps
clock = pygame.time.Clock()
clock.tick(60)

#Player
playerImg=pygame.image.load("char.png")
playerImg2=pygame.image.load("char1.png")
playerX=100
playerY=675
playerX_change=0
playerY_change=0

def player(x,y):
    screen.blit(playerImg,(x,y))


#Ttile and icon
pygame.display.set_caption("Graveyard")
icon=pygame.image.load("TombStone.png")
background=pygame.image.load("bg.png")
'''tiles1=pygame.image.load("images/png/Tiles/tile--1-.png")
tiles2=pygame.image.load("images/png/Tiles/tile--2-.png")
tiles3=pygame.image.load("images/png/Tiles/tile--3-.png")
tiles4=pygame.image.load("images/png/Tiles/tile--4-.png")
tiles5=pygame.image.load("images/png/Tiles/tile--5-.png")
tiles6=pygame.image.load("images/png/Tiles/tile--6-.png")
tiles7=pygame.image.load("images/png/Tiles/tile--7-.png")
tiles8=pygame.image.load("images/png/Tiles/tile--8-.png")
tiles9=pygame.image.load("images/png/Tiles/tile--9-.png")
tiles10=pygame.image.load("images/png/Tiles/tile--10-.png")
tiles11=pygame.image.load("images/png/Tiles/tile--11-.png")
tiles12=pygame.image.load("images/png/Tiles/tile--12-.png")
tiles13=pygame.image.load("images/png/Tiles/tile--13-.png")
tiles14=pygame.image.load("images/png/Tiles/tile--14-.png")
tiles15=pygame.image.load("images/png/Tiles/tile--15-.png")
tiles16=pygame.image.load("images/png/Tiles/tile--16-.png")'''
tiles17=pygame.image.load("images/png/Tiles/bg-example.png")
bg_plt= pygame.transform.scale(tiles17, (1500, 700))
pygame.display.set_icon(icon)

#Gameloop
Gameloop=True
while Gameloop:
    #Background
    screen.fill((48,25,52))
    screen.blit(background,(0,0))
    '''screen.blit(tiles1,(100,100))
    screen.blit(tiles2,(100,505))'''
    screen.blit(bg_plt,(0,100))
    playerY+=10
    
    for event in pygame.event.get():
        #Closing the Window
        if event.type==pygame.QUIT:
            Gameloop= False
            pygame.quit()
      
        #Character Movements
        #Movement Starts
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change= -7
                playerImg=playerImg2
                
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change= 7
                playerImg=playerImg
                
        
            if event.key == pygame.K_UP or event.key == pygame.K_w:            
                playerY_change= -7
            '''if event.key == pygame.K_DOWN or event.key == pygame.K_s:            
                playerY_change= 10'''
                
        #Movement Stops     
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerX_change= 0
                playerY_change= 0
    
    playerX += playerX_change
    playerY += playerY_change
    
    #Boundaries to the game
    if playerX <=0:
            playerX=0
    if playerX >=1430:
            playerX=1430
    '''if playerY <=-100:
            playerY=-100'''
    if playerY >=800:
            playerY=800   
            
    player(playerX,playerY)
    
    pygame.display.update()
    