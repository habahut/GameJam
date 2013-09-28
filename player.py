#!usr/bin/env python

from pygame import Rect
from math import sqrt
from weapon import *

class Player:
    def __init__(self, x, y, weapon):
        self.dx = 0
        self.dy = 0
        self.lungetimer = 0
        self.lungedelay = 500
        self.myrect = Rect(x,y,32,32)
        self.currentWeapon = weapon
    
    def update(self, dt):
        self.myrect.centerx += (self.dx * dt)
        self.myrect.centery += (self.dy * dt)
        self.lungetimer -= dt        
        self.currentWeapon.update(dt)

        if self.lungetimer >= 400:
            self.dy *= .8
            self.dx *= .8
        elif self.lungetimer >= 175:
            self.dy *= .6
            self.dx *= .6
        else:
            self.dy = 0
            self.dx = 0

    def lunge(self, mx, my):
        if self.lungetimer > 0:
            return

        self.lungetimer = self.lungedelay
        dirX = mx - 500
        dirY = my - 350

        d = sqrt(dirX * dirX + dirY * dirY)
        dirX /= d
        dirX *= 7
        dirY /= d
        dirY *= 7

        self.dx += dirX
        self.dy += dirY

    def setWeapon(self, weapon):
        self.currentWeapon = weapon

    def shoot(self):
        return self.currentWeapon.shoot()
        



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

