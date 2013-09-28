#!usr/bin/env python

import pygame
from pygame.locals import *
from player import Player
from dinosaur import Dinosaur
from mouse import *

SCREEN_SIZE = 600,600
WHITE = 255,255,255

pygame.init()
global screen
screen = pygame.display.set_mode(SCREEN_SIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)
screen.fill((255,255,255))

clock = pygame.time.Clock()
FPS = 60

pygame.key.set_repeat(10,10)

dino = Dinosaur(500,500)

player = Player()
playerimage = pygame.image.load("ICON2.bmp").convert()

## lists
bullets = []
dinos = []
done = False
while not done:
    dt = float(clock.tick(FPS)) / 5
    mx, my = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN:
            if event.key == K_w:
                player.setDY(-1)
            elif event.key == K_a:
                player.setDX(-1)
            elif event.key == K_s:
                player.setDY(1)
            elif event.key == K_d:
                player.setDX(1)
            elif event.key == K_SPACE:
                player.lunge(mx,my)
            

    screen.fill((255,255,255))
    #pygame.draw.circle(screen, (0,0,0), (int(player.getX()), int(player.getY())), 5)
    screen.blit(playerimage, (int(player.getX()), int(player.getY())))
    pygame.draw.circle(screen, (0,0,0), (int(dino.getX()), int(dino.getY())), 5)
    pygame.display.flip()

    ## game logic
    dino.decide(player.getX(), player.getY())
    dino.update(dt)
    player.update(dt)
    
    ## collission detection
    
    

pygame.quit()



