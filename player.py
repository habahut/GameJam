#!usr/bin/env python

from math import sqrt

class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.dx = 0
        self.dy = 0
        self.lungetimer = 0
        self.lungedelay = 500

    def update(self, dt):
        self.x += (self.dx * dt)
        self.y += (self.dy * dt)
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
        dirX *= 8
        dirY /= d
        dirY *= 8

        self.dx += dirX
        self.dy += dirY

    def getWeapon(self):
        return 1




    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y

    def setDX(self, dx):
        self.dx = dx
    def setDY(self, dy):
        self.dy = dy
    def getDX(self, dx):
        return self.dx
    def getDY(self, dy):
        return self.dy

