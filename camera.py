#!usr/bin/env python

from pygame import Rect
import pygame
from tiledImage import TiledImage
import random

class Camera:

    def __init__(self, screen, screensize, playerpos, tileImage, tileSize, currentWeapon):
        self.screen = screen
        self.screensize = screensize
        self.playerx,self.playery = playerpos
        self.halfscreenx,self.halfscreeny = screensize
        self.halfscreenx /= 2
        self.halfscreeny /= 2
        self.rect = Rect(self.playerx-self.halfscreenx, self.playery-self.halfscreeny, self.halfscreenx * 2, self.halfscreeny * 2)
        self.tiledImage = tileImage
        self.tileSize = tileSize
        self.dpx = 0
        self.dpy = 0
        self.currentWeapon = currentWeapon
        self.goreObjects = []

    def changeWeapon(self, cw):
        self.currentWeapon = cw

    def registerGore(self, go):
        self.goreObjects.append(go)
        
    def update(self, playerx, playery, dt):
        self.dpx += self.playerx - playerx
        self.dpy += self.playery - playery
        self.playerx = playerx
        self.playery = playery
        self.rect.top = playery - self.halfscreeny
        self.rect.left = playerx - self.halfscreenx
        if self.tiledImage != None:
            r = self.screen.get_rect()
            rect = Rect(r.top - 2 * self.tileSize, r.left - 2 * self.tileSize,
                                r.width + 2 * self.tileSize, r.height + 2 * self.tileSize)
            rect.centerx += self.dpx
            rect.centery += self.dpy
            self.tiledImage.draw(self.screen, rect)

        toRemove = []
        for i,gore in enumerate(self.goreObjects):
            x = gore.getX() - self.rect.left
            y = gore.getY() - self.rect.top
            self.screen.blit(gore.getScreen(), (x,y))
            if gore.update(dt):
                toRemove.append(i)

        for i in toRemove:
            del self.goreObjects[i]

        self.screen.blit(self.currentWeapon, (15,15))
        

    def drawList(self, objList, img):
        toRemove = []
        for i in range(len(objList)):
            if not self.rect.colliderect(objList[i].getRect()):
                toRemove.append(i)
                continue
            relposx = objList[i].getX() - self.rect.left
            relposy = objList[i].getY() - self.rect.top

            timer = objList[i].getInviTimer()
            if (timer>150):
                self.screen.blit(img, (int(relposx),int(relposy)))

        for i in reversed(toRemove):
            objList.pop(i)

    def drawPlayer(self, playerimage):
        self.screen.blit(playerimage, (self.halfscreenx,self.halfscreeny))

    def drawObj(self, obj, img):
        if not self.rect.colliderect(obj.getRect()):
            return
        relposx = obj.getX()
        relposy = obj.getY()

        self.screen.blit(img, (relposx,relposy))

    def drawBulletList(self, objList):
        toRemove = []
        for i in range(len(objList)):
            if not self.rect.collidepoint(objList[i].getX(), objList[i].getY()):
                toRemove.append(i)
                continue
            relposx = objList[i].getX() - self.rect.left
            relposy = objList[i].getY() - self.rect.top
            pygame.draw.circle(self.screen, (0,0,0), (int(relposx), int(relposy)), 5)

        for i in reversed(toRemove):
            del objList[i]





        
