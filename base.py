#!usr/bin/env python

import pygame
from pygame.locals import *
from player import Player
from dinosaur import Dinosaur
from weapon import Weapon
from camera import Camera
import random

SCREEN_SIZE = 1000,700
WHITE = 255,255,255

pygame.init()
global screen
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((255,255,255))

playerstartx,playerstarty = 100,100

clock = pygame.time.Clock()
FPS = 60

pygame.key.set_repeat(10,10)

player = Player(100,100)
playerimage = pygame.image.load("ICON2.bmp").convert()
dinoimage = pygame.image.load("dino_right.bmp").convert()
dinoimage.set_colorkey((0,0,0))


## lists
bullets = []
projectileList = []
dinoList = []
dinoList.append(Dinosaur(700,700))

done = False

camera = Camera(screen, SCREEN_SIZE, (playerstartx,playerstarty))
while not done:
    mx,my = pygame.mouse.get_pos()
    dt = float(clock.tick(FPS)) / 5
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
            elif event.key == K_SPACE:
                player.lunge(mx,my)
        elif event.type == MOUSEBUTTONDOWN:
            projectile = Weapon(int(player.getX()), int(player.getY()),(mx,my))
            print mx,my
            projectileList.append(projectile)
  
    screen.fill((255,255,255))
    camera.update(player.getX(), player.getY())
    camera.drawBulletList(projectileList)
    camera.drawList(dinoList, dinoimage)
    camera.drawPlayer(playerimage)
    pygame.display.flip()

    ## game logic
    player.update(dt)
    for d in dinoList:
        d.decide(player.getX(), player.getY())
        d.update(dt)
    
    ## collission detection
    toRemove = []
    for projectile in projectileList:
        projectile.update(dt)
        for i in range(len(dinoList)):
            if dinoList[i].getRect().colliderect(pygame.Rect(int(projectile.getX()), int(projectile.getY()), 2,2)) == True:
                #dino.getHit(projectile)
                toRemove.append(i)

    for i in toRemove:
        dinoList.pop(i)

    for i in range(len(dinoList), 5):
        newx = random.randint(-SCREEN_SIZE[0] / 2, SCREEN_SIZE[0] / 2)
        newy = random.randint(-SCREEN_SIZE[1] / 2, SCREEN_SIZE[1] / 2)
        dinoList.append(Dinosaur(newx, newy))
        
        
                
    

pygame.quit()



