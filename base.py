#!usr/bin/env python

import pygame
from pygame.locals import *
from player import Player
from dinosaur import Dinosaur
from weapon import Weapon
import weapon

SCREEN_SIZE = 1000,700
WHITE = 255,255,255

pygame.init()
global screen
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((255,255,255))

clock = pygame.time.Clock()
FPS = 60

pygame.key.set_repeat(10,10)

dino = Dinosaur(700,1000)
dinoleft = pygame.image.load("dino_right.bmp")
dinoright = pygame.image.load("dino_right.bmp")



player = Player(100,100)
playerimage = pygame.image.load("ICON2.bmp").convert()

## lists
bullets = []
dinoList = []
projectileList = []
weaponType = 2
factory = weapon.WeaponFactory()

dinoList.append(dino)
done = False
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
            elif event.key == K_h:
                projectile = factory.createProjectile(int(player.getX()), int(player.getY()),pygame.mouse.get_pos(), weaponType)
                projectileList.append(projectile)
  
    screen.fill((255,255,255))  
    if not len(projectileList)<1:
        for projectile in projectileList:
            pygame.draw.circle(screen, (0,0,0), (int(projectile.getX()), int(projectile.getY())), 5)
    screen.blit(playerimage, (int(player.getX()), int(player.getY())))
    screen.blit(dinoleft, (int(dino.getX()), int(dino.getY())))
    pygame.display.flip()

    ## game logic
    dino.decide(player.getX(), player.getY())


    ## collider
    player.update(dt)
    dino.update(dt)
    
    ## collission detection
    toRemove = []
    for projectile in projectileList:
        projectile.update(dt)
        # for i in range(len(dinoList), 0, -1):
            # if dino.getrect().colliderect(pygame.Rect(int(projectile.getX()), int(projectile.getY()), 2,2)) == True:
                # dino.getHit(projectile)
                # toRemove.append(i)

    # for i in toRemove:
    #     dinolist.
                
                
    

pygame.quit()



