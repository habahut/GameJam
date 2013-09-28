#!usr/bin/env python

from pygame import Rect
import pygame

class Camera:

    def __init__(self, screen, screensize, playerpos):
        self.screen = screen
        self.screensize = screensize
        x,y = playerpos
        self.halfscreenx,self.halfscreeny = screensize
        self.halfscreenx /= 2
        self.halfscreeny /= 2
        self.rect = Rect(x-self.halfscreenx, y-self.halfscreeny, self.halfscreenx * 2, self.halfscreeny * 2)

    def update(self, playerx, playery):
        self.playerx = playerx
        self.playery = playery
        self.rect.top = playery - self.halfscreeny
        self.rect.left = playerx - self.halfscreenx

    def drawList(self, objList, img):
        toRemove = []
        for i in range(len(objList)):
            if not self.rect.colliderect(objList[i].getRect()):
                toRemove.append(i)
                continue
            relposx = objList[i].getX() - self.rect.left
            relposy = objList[i].getY() - self.rect.top

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
            objList.pop(i)





        
