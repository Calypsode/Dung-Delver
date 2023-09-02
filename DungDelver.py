
#Imports

import pygame, os, sys
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()


# GLOBAL VARIABLES

WHITE = (255,255,255)
BROWN = (102,51,0)
TAN = (255,229,204)
BLACK = (0,0,0)
x = 20
y = 20


#Screen

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Dung Delver")




# Sprites

dm = pygame.image.load('Dungmador.jpg')
dm = pygame.transform.scale(dm, (50,70))


#Movement

dm_rect = dm.get_rect()
        

#Main Loop

running = True
while running:
    
    
    keys = pygame.key.get_pressed()    
    screen.blit(dm, (x,y))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit


    if keys[pygame.K_LEFT]:
        x-=.1
    if keys[pygame.K_RIGHT]:
        x+=.1    


    screen.fill((WHITE))
    pygame.display.update()



pygame.quit()
quit()

        
        


    
    




