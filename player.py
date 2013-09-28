#!usr/bin/env python

from pygame import Rect
from math import sqrt

class Player:
    def __init__(self, x, y):
        self.dx = 0
        self.dy = 0
        self.lungetimer = 0
        self.lungedelay = 500
        self.myrect = Rect(x,y,32,32)
    
    def update(self, dt):
        #self.myrect.centerx += (self.dx * dt)
        self.myrect.centerx += (self.dx * dt)
        self.myrect.centery += (self.dy * dt)
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
        if self.lungetimer > 0:
            return

        self.lungetimer = self.lungedelay
        dirX = mx - self.myrect.centerx
        dirY = my - self.myrect.centery

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
        return self.myrect.centerx
    def getY(self):
        return self.myrect.centery
    def setX(self, x):
        self.myrect.centerx = x
    def setY(self, y):
        self.myrect.centery = y
    def getRect(self):
        return self.myrect

    def setDX(self, dx):
        self.dx = dx
    def setDY(self, dy):
        self.dy = dy
    def getDX(self, dx):
        return self.dx
    def getDY(self, dy):
        return self.dy

