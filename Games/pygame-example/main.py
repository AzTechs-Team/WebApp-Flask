import pygame
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
player_Jump=False

def player(x,y):
    screen.blit(playerImg,(x,y))


#Ttile Background and icon
pygame.display.set_caption("Graveyard")
icon=pygame.image.load("TombStone.png")
background=pygame.image.load("bg.png")
tiles17=pygame.image.load("images/png/Tiles/bg-example.png")
bg_plt= pygame.transform.scale(tiles17, (1500, 700))
pygame.display.set_icon(icon)



#Gameloop
Gameloop=True
while Gameloop:
    #Background
    screen.fill((48,25,52))
    screen.blit(background,(0,0))
    screen.blit(bg_plt,(0,100))
    playerY+=5
    
    for event in pygame.event.get():
        #Closing the Window
        if event.type==pygame.QUIT:
            Gameloop= False
            pygame.quit()
      
        #Character Movements
        #Movement Starts
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change= -6
                
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change= 6
                
        
            if event.key == pygame.K_UP or event.key == pygame.K_w:            
                playerY_change= -20
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
    if playerY >=680:
            playerY=680
            
    player(playerX,playerY)
    pygame.display.update()
    