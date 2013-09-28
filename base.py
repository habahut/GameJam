#!usr/bin/env python

import pygame
from pygame.locals import *
from player import Player
from dinosaur import Dinosaur
from weapon import Weapon

SCREEN_SIZE = 600,600
WHITE = 255,255,255

pygame.init()
global screen
player = Player()
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((255,255,255))

clock = pygame.time.Clock()
FPS = 60

pygame.key.set_repeat(10,10)

dino = Dinosaur(1000,700)
dinoleft = pygame.image.load("dino_left.bmp")
dinoright = pygame.image.load("dino_right.bmp")



player = Player(100,100)
playerimage = pygame.image.load("ICON2.bmp").convert()

## lists
bullets = []
dinos = []

done = False
projectileList = []
while not done:
    dt = float(clock.tick(FPS)) / 50
    
    screen.fill((255,255,255))
    

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
            elif event.key == K_h:
                projectile = Weapon(int(player.getX()), int(player.getY()),pygame.mouse.get_pos())
                projectileList.append(projectile)
                pygame.draw.circle(screen, (0,0,0), (int(projectile.getX()), int(projectile.getY())), 5)


    
    if not len(projectileList)<1:
        for projectile in projectileList:
            pygame.draw.circle(screen, (0,0,0), (int(projectile.getX()), int(projectile.getY())), 5)
    

    screen.fill((255,255,255))
    #pygame.draw.circle(screen, (0,0,0), (int(player.getX()), int(player.getY())), 5)
    screen.blit(playerimage, (int(player.getX()), int(player.getY())))
    #pygame.draw.circle(screen, (0,0,0), (int(dino.getX()), int(dino.getY())), 5)
    screen.blit(dinoleft, (int(dino.getX()), int(dino.getY())))
    pygame.display.flip()

    ## game logic
    dino.decide(player.getX(), player.getY())


    ## collider
    player.update(dt)


    
    ## collission detection
    
    
    



    if not len(projectileList)<1:
        for projectile in projectileList:
            projectile.update(dt)
    #collider.update(dt)





