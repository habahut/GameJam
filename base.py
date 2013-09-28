#!usr/bin/env python

import pygame
from pygame.locals import *
pygame.init()
SCREEN_SIZE = 1000,700
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((255,255,255))

from player import Player
from dinosaur import *
from camera import Camera
import random
from weapons import *
from projectiles import Projectile
import time
from tiledImage import TiledImage
from goreSplatter import GoreSplatter


WHITE = 255,255,255

playerstartx,playerstarty = 100,100

clock = pygame.time.Clock()
FPS = 60

pygame.key.set_repeat(10,10)

currentWeapon = MachineGun()
player = Player(100,100, currentWeapon)
playerimage = pygame.image.load("ICON2.bmp").convert()
playerimage.set_colorkey((255,255,255))
dinoimage = pygame.image.load("dino_right.bmp").convert()
dinoimage.set_colorkey((48,120,128))

## body part images:
bodyParts = []
bodyParts.append(pygame.image.load("eyeball.bmp").convert())
bodyParts[0].set_colorkey((0,0,0))
bodyParts.append(pygame.image.load("limb1.bmp").convert())
bodyParts[1].set_colorkey((0,0,0))
bodyParts.append(pygame.image.load("limb2.bmp").convert())
bodyParts[2].set_colorkey((0,0,0))
bodyParts.append(pygame.image.load("limb3.bmp").convert())
bodyParts[3].set_colorkey((0,0,0))
bodyParts.append(pygame.image.load("limb4.bmp").convert())
bodyParts[4].set_colorkey((0,0,0))
bodyParts.append(pygame.image.load("limb5.bmp").convert())
bodyParts[5].set_colorkey((0,0,0))
bodyParts.append(pygame.image.load("limb6.bmp").convert())
bodyParts[6].set_colorkey((0,0,0))
bodyParts.append(pygame.image.load("limb7.bmp").convert())
bodyParts[7].set_colorkey((0,0,0))

## sounds
pygame.mixer.init()
sounds = {}
sounds['cutthemdown'] = pygame.mixer.Sound("cutthemdown.ogg")
sounds['datlaugh'] = pygame.mixer.Sound("datlaugh.ogg")
sounds['leavetheminpieces'] = pygame.mixer.Sound("leavetheminpeices.ogg")
sounds['carnage'] = pygame.mixer.Sound("carnage.ogg")
sounds['swings'] = pygame.mixer.Sound("swings.ogg")


## weapon images
weaponImages = {}
weaponImages['rocketlauncher'] = pygame.image.load("bazooka.png").convert()
weaponImages['rocketlauncher'].set_colorkey((0,0,0))
weaponImages['bow'] = pygame.image.load("bow_icon.png").convert()
weaponImages['bow'].set_colorkey((255,255,255))
weaponImages['sword'] = pygame.image.load("sword.png").convert()
weaponImages['sword'].set_colorkey((211,149,188))
weaponImages['minigun'] = pygame.image.load("minigun.png").convert()
weaponImages['minigun'].set_colorkey((0,0,0))

## bullet images
bulletImages = {}

bulletImages['sword'] = pygame.image.load("sword.png").convert()
bulletImages['sword'].set_colorkey((255,255,255))

## lists
bullets = []
projectileList = []
dinoList = []
dinoList.append(Dinosaur(700,700))


timeLock = 0

done = False
shooting = False

camera = Camera(screen, SCREEN_SIZE, (playerstartx,playerstarty), TiledImage(pygame.image.load("grasstile.bmp").convert()), 100, weaponImages['minigun'])
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
            elif event.key == K_1:
                currentWeapon = Bow()
                player.setWeapon(currentWeapon)
                camera.setCurrentWeapon(weaponImages['bow'])
                if not pygame.mixer.get_busy():
                    sounds['carnage'].play()
            elif event.key == K_2:
                currentWeapon = MachineGun()
                player.setWeapon(currentWeapon)
                camera.setCurrentWeapon(weaponImages['minigun'])
                if not pygame.mixer.get_busy():
                    sounds['datlaugh'].play()
            elif event.key == K_3:
                #currentWeapon = FUCKINGSWORD()
                #player.setWeapon(currentWeapon)
                #camera.setCurrentWeapon(weaponImages['sword'])
                pass
            elif event.key == K_4:
                currentWeapon = RocketLauncher()
                player.setWeapon(currentWeapon)
                camera.setCurrentWeapon(weaponImages['rocketlauncher'])
                if not pygame.mixer.get_busy():
                    sounds['leavetheminpieces'].play()
        elif event.type == MOUSEBUTTONDOWN:
            shooting = True
        elif event.type == MOUSEBUTTONUP:
            shooting = False
            
    if shooting:
        projectile = player.shoot()
        if projectile != None:
            projectile.setTrajectory(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2, mx,my)
            projectile.setImage(currentWeapon.makeImage(projectile.getDX(), projectile.getDY()))
            projectile.setpos(player.getX(), player.getY())
            projectileList.append(projectile)
  
    screen.fill((255,255,255))
    camera.update(player.getX(), player.getY(), dt)
    camera.drawBulletList(projectileList)
    camera.drawList(dinoList, dinoimage)
    camera.drawPlayer(playerimage)   
    pygame.display.flip()

    ## game logic
    player.update(dt)
    for d in dinoList:
        d.decide(player.getX(), player.getY())
        d.update(dt)

    for projectile in projectileList:
        projectile.update(dt)

    """ need to do ray casting here... some (read, almost all) go through the dinos instead of hitting them... """             
    
    ## collission detection
    impacts = []
    for p in range(len(projectileList)):
        for i in range(len(dinoList)):
            if dinoList[i].getRect().colliderect(projectileList[p].getRect()) == True:
                #dino.getHit(projectileList[p].getDamage())
                impacts.append([projectileList[p],p,dinoList[i]])
                break

    for impact in impacts:
        impact = impact[0]
        hitType = impact.getHitType()
        if hitType == 0:
            camera.registerGore(GoreSplatter(impact.getX(), impact.getY(), impact.getDX(), impact.getDY(),
                                         impact.getImpact(), hitType, bodyParts[random.randint(0, len(bodyParts) - 1)]))
            #continue ## nothing special
        if hitType == 1: ## BOOM BABY
            ## GONE MAKE DAT EXPLOSION SON!!!!!!!!!
            
            camera.registerGore(GoreSplatter(impact.getX(), impact.getY(), impact.getDX(), impact.getDY(),
                                         impact.getImpact(), hitType, bodyParts[random.randint(0, len(bodyParts) - 1)]))
        if hitType == 2: ## piercing
            camera.registerGore(GoreSplatter(impact.getX(), impact.getY(), impact.getDX(), impact.getDY(),
                               impact.getImpact(), hitType, bodyParts[random.randint(0, len(bodyParts) - 1)]))

    if len(impacts) > 0:
        if not pygame.mixer.get_busy():
            if (random.randint(0,10000) > 9900):
                t = random.randint(0,1)
                if t == 0:
                    sounds['cutthemdown'].play()
                else:
                    sounds['swings'].play()

    #for impact in impacts:
    #      p = impact[1]
    #      del projectileList[p]

    for impact in impacts:
        p = impact[1]
        d = impact[2]
        if d.getShieldTimer() > 300:
            projectileList[p].setDxDy( (0 - projectileList[p].getDX()), (0 - projectileList[p].getDY()))
            impacts.remove(impact)
        else:
            if impact[0] in projectileList:
                projectileList.remove(impact[0])
            if d in dinoList:
                dinoList.remove(d)


    for i in range(len(dinoList), 1):#5
        newx = random.randint(-SCREEN_SIZE[0] / 2, SCREEN_SIZE[0] / 2)
        newy = random.randint(-SCREEN_SIZE[1] / 2, SCREEN_SIZE[1] / 2)
        #dinoList.append(Dinosaur(newx, newy))    
        #dinoList.append(Invi_Dino(newx, newy))    
        #dinoList.append(Jump_Dino(newx, newy))    
        dinoList.append(Shield_Dino(newx, newy))    

pygame.quit()



