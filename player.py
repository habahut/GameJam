#!usr/bin/env python

from pygame import rect
from math import sqrt

class Player:
    def __init__(self, x, y):
        self.dx = 0
        self.dy = 0
        self.lungetimer = 0
        self.lungedelay = 500
        self.rect = (x,y,32,32)

    def update(self, dt):
        self.rect.centerx += (self.dx * dt)
        self.rect.centery += (self.dy * dt)
        self.lungetimer -= dt
        if self.lungetimer >= 400:
            self.dy *= .8
            self.dx *= .8
        elif self.lungetimer >= 175:
            self.dy *= .6
            self.dx *= .6
        else:
            self.dy *= .5
            self.dx *= .5

    def lunge(self, mx, my):
        print self.lungetimer
        if self.lungetimer > 0:
            return

        self.lungetimer = self.lungedelay
        dirX = mx - self.x
        dirY = my - self.y

        d = sqrt(dirX * dirX + dirY * dirY)
        dirX /= d
        dirX *= 7
        dirY /= d
        dirY *= 7

        self.dx += dirX
        self.dy += dirY

    def getWeapon(self):
        return 1




    def getX(self):
        return self.rect.centerx
    def getY(self):
        return self.rect.centery
    def setX(self, x):
        self.rect.centerx = x
    def setY(self, y):
        self.rect.centery = y

    def setDX(self, dx):
        self.dx = dx
    def setDY(self, dy):
        self.dy = dy
    def getDX(self, dx):
        return self.dx
    def getDY(self, dy):
        return self.dy

